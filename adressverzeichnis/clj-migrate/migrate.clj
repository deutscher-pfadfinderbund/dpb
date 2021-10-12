#!/usr/bin/env bb

(ns migrate
  (:require
   [babashka.deps :as deps]
   [clojure.pprint :as pprint]
   [clojure.string :as str]
   [clojure.set :as set]
   [clojure.java.io :as io]
   [flatland.ordered.map :refer [ordered-map]])
  (:import java.util.Date))

(deps/add-deps 
 '{:deps 
   {com.github.seancorfield/honeysql {:mvn/version "2.1.818"}
    org.clojure/data.csv {:mvn/version "1.0.0"}}})

(require '[clojure.data.csv :as csv]
         '[honey.sql :as sql]
         '[honey.sql.helpers :as helpers :refer [select insert-into values from where on-conflict do-nothing]])

(def path-to-csv (first *command-line-args*))

(defn remove-empty-or-nil-fields [m]
  (into {} (remove (comp str/blank? second)) m))

(defn csv-data->maps [csv-data]
  (map remove-empty-or-nil-fields
    (map zipmap
       (->> (first csv-data) ;; First row is the header
            (map keyword) ;; Drop if you want string keys instead
            repeat)
       (rest csv-data))))

(def old
  (csv-data->maps
   (with-open [reader (io/reader path-to-csv)]
    (doall
     (csv/read-csv reader)))))

(def rename-keys
  {:Anrede :anrede
   :Titel :titel
   :Vorname :vorname
   :Nachname :nachname
   :Fahrtenname :fahrtenname
   :Email :email
   :NRW :nrw
   :Stand :stand
   :NichtAbdrucken :nicht_abdrucken
   :Anmerkung :anmerkung
   :Geburtsdatum :geburtstag
   :Todesdatum :todestag
   :ID :alte_id})

(def stand-map
  {"OR" "Ordensritter"
   "P" "Pilgerin"
   "StGR" "St.-Georgs-Ritter"
   "GM" "Gildenmeisterin"
   "Gim" "Gildenmädchen"
   "Gil" "Gildin"})

(defn parse-date [s]
  (when-not (str/blank? s)
    (let [[_ date year month day] (re-find #"^((\d\d\d\d)-(\d\d)-(\d\d))" s)]
      date)))

(defn get-adress [{:keys [Straße Zusatz Postleitzahl Ort]}]
  (when-not (every? str/blank? [Straße Zusatz Postleitzahl Ort])
    {:label ""
     :strasse (or Straße "")
     :zusatz (or Zusatz "")
     :plz (or Postleitzahl "")
     :stadt (or Ort "")
     :land "Deutschland"}))

(defn build-number [vorwahl nummer]
  (str vorwahl nummer))

(defn get-numbers [{:keys [Vorwahl1 Telefonnummer1 Telefonbezeichner1
                           Vorwahl2 Telefonnummer2 Telefonbezeichner2
                           Vorwahl3 Telefonnummer3 Telefonbezeichner3]}]
  (let [not-blank? (complement str/blank?)]
    (cond-> []
      (not-blank? Telefonnummer1)
      (conj {:label (or Telefonbezeichner1 "")
             :nummer (build-number Vorwahl1 Telefonnummer1)})
      
      (not-blank? Telefonnummer2)
      (conj {:label (or Telefonbezeichner2 "")
             :nummer (build-number Vorwahl2 Telefonnummer2)})
      
      (not-blank? Telefonnummer3)
      (conj {:label (or Telefonbezeichner3 "")
             :nummer (build-number Vorwahl3 Telefonnummer3)}))))

(defn parse-out-tel [person]
  (-> person
      (assoc :numbers (get-numbers person))
      (dissoc :Vorwahl1 :Telefonnummer1 :Telefonbezeichner1 
              :Vorwahl2 :Telefonnummer2 :Telefonbezeichner2 
              :Vorwahl3 :Telefonnummer3 :Telefonbezeichner3)))

(defn parse-out-adress [person]
  (-> person
      (assoc :address (get-adress person))
      (dissoc :Straße :Zusatz :Postleitzahl :Ort)))

(defn get-permissions [{:keys [Bundesthing Bundesrat Bundesjungenrat Bundesmädchenrat]
                        :as person}]
  {"Bundesthing" 
   {:bekommt_einladung (Boolean/parseBoolean Bundesthing)
    :hat_stimmrecht (Boolean/parseBoolean (get person (keyword "Stimmberechtigung Bundesthing")))
    :bekommt_protokoll (Boolean/parseBoolean (get person (keyword "Protokoll Bundesthing")))}
   "Bundesrat"
   {:bekommt_einladung (Boolean/parseBoolean Bundesrat)
    :hat_stimmrecht (Boolean/parseBoolean (get person (keyword "Stimmberechtigung Bundesrat")))
    :bekommt_protokoll (Boolean/parseBoolean (get person (keyword "Protokoll Bundesrat")))}
   "Bundesmädchenrat"
   {:bekommt_einladung (Boolean/parseBoolean Bundesmädchenrat)
    :hat_stimmrecht (Boolean/parseBoolean (get person (keyword "Stimmberechtigung Bundesmädchenrat")))
    :bekommt_protokoll (Boolean/parseBoolean (get person (keyword "Protokoll Bundesmädchenrat")))}
   "Bundesjungenrat"
   {:bekommt_einladung (Boolean/parseBoolean Bundesjungenrat)
    :hat_stimmrecht (Boolean/parseBoolean (get person (keyword "Stimmberechtigung Bundesjungenrat")))
    :bekommt_protokoll (Boolean/parseBoolean (get person (keyword "Protokoll Bundesjungenrat")))}})

(defn parse-out-permissions [person]
  (-> person
      (assoc :permissions (get-permissions person))
      (dissoc
       :Bundesthing (keyword "Protokoll Bundesthing") (keyword "Stimmberechtigung Bundesthing")
       :Bundesrat (keyword "Protokoll Bundesrat") (keyword "Stimmberechtigung Bundesrat")
       :Bundesjungenrat (keyword "Protokoll Bundesjungenrat") (keyword "Stimmberechtigung Bundesjungenrat")
       :Bundesmädchenrat (keyword "Protokoll Bundesmädchenrat") (keyword "Stimmberechtigung Bundesmädchenrat"))))

(defn parse-person [person]
  (-> person
      parse-out-tel
      parse-out-adress
      parse-out-permissions
      (set/rename-keys rename-keys)
      (update :geburtstag parse-date)
      (update :todestag parse-date)
      (update :nrw #(Boolean/parseBoolean %))
      (update :nicht_abdrucken #(Boolean/parseBoolean %))
      (update :stand #(get stand-map % nil))))


;;;; SQL-Map generation functions

(defn valid-amttyp [amt]
  (when amt
    (cond
      (or (str/includes? amt "führer")
          (str/includes? amt "vogt")
          (str/includes? amt "vögtin")) "Führer:in/Vögtin/Vogt"
      (re-matches #"(?i).*kanzler.*" amt) "Kanzler:in"
      (re-matches #"(?i).*kämmer.*" amt) "Kämmerin/Kämerer"
      :else amt)))

(defn amttypen-sql [persons]
  (-> (insert-into :public.adressverzeichnis_amttyp)
      (values (cons {:name "Mitglied"}
                    (for [amt (set (keep (comp valid-amttyp :Amt) persons))]
                      {:name amt})))))

(defn ämter [persons]
  (-> (insert-into :public.adressverzeichnis_amt)
      (values (for [{:keys [Amt Gruppe alte_id]} persons
                    :let [norm-amt (valid-amttyp Amt)]
                    :when norm-amt]
                {:bestaetigt true
                 :gruppierung_id
                 (-> (select :id) (from :public.adressverzeichnis_gruppierung) (where [:= :name Gruppe]))
                 :typ_id
                 (-> (select :id) (from :public.adressverzeichnis_amttyp) (where [:= :name norm-amt]))
                 :person_id
                 (-> (select :id) (from :public.adressverzeichnis_person) (where [:= :alte_id alte_id]))}))))

(defn ordensmitgliedschaften-sql [persons]
  (-> (insert-into :public.adressverzeichnis_amt)
      (values
       (for [{:keys [Ordensgruppe alte_id]} persons
             :when Ordensgruppe]
         {:bestaetigt false
          :gruppierung_id 
          (-> (select :id) (from :public.adressverzeichnis_gruppierung) (where [:= :name Ordensgruppe]))
          :person_id
          (-> (select :id) (from :public.adressverzeichnis_person) (where [:= :alte_id alte_id]))
          :typ_id
          (-> (select :id) (from :public.adressverzeichnis_amttyp) (where [:= :name "Mitglied"]))}))))

(defn addresses-sql [persons]
  (-> (insert-into :public.adressverzeichnis_adresse)
      (values (for [{:keys [address alte_id]} persons
                    :when address]
                (assoc address
                       :person_id
                       (-> (select :id)
                           (from :public.adressverzeichnis_person)
                            (where [:= :alte_id alte_id])))))))

(defn phones-sql [persons]
  (-> (insert-into :public.adressverzeichnis_telefon)
      (values
       (apply concat
        (for [{:keys [numbers alte_id]} persons]
          (for [phone numbers]
            (assoc phone
                   :person_id
                   (-> (select :id)
                       (from :public.adressverzeichnis_person)
                       (where [:= :alte_id alte_id])))))))))

(defn persons-sql [persons]
  (-> (insert-into :public.adressverzeichnis_person)
      (values 
       (map #(merge 
              {:anmerkung ""
               :anrede ""
               :titel ""
               :vorname ""
               :fahrtenname ""
               :nachname ""}
              (select-keys % #{:stand :anmerkung :email :nicht_abdrucken :geburtstag :titel :fahrtenname :nachname :alte_id :todestag :vorname :nrw :anrede}))
          persons))))

(def organe #{"Bundesrat" "Bundesmädchenrat" "Bundesjungenrat" "Bundesthing"})

(defn organs-sql []
  (-> (insert-into :public.adressverzeichnis_organ)
      (values (for [organ organe]
                {:name organ}))))

(defn permission-sql [permissions alte_id]
  (for [[organ permission] permissions
        :when (some true? (map second permission))]
    (assoc permission
           :organ_id (-> (select :id) (from :public.adressverzeichnis_organ) (where [:= :name organ]))
           :person_id (-> (select :id) (from :public.adressverzeichnis_person) (where [:= :alte_id alte_id])))))

(defn pemissions-sql [persons]
  [(organs-sql)
   (-> (insert-into :public.adressverzeichnis_manuelleberechtigung)
       (values
        (apply concat 
          (for [{:keys [permissions alte_id]} persons]
            (permission-sql permissions alte_id)))))])

(defn ordensgruppe-typ [ordensgruppe]
  (and ordensgruppe
    (cond
      (str/includes? ordensgruppe "Konvent") "Konvent"
      (str/includes? ordensgruppe "Aufbaukollegium") "Aufbaukollegium"
      (str/includes? ordensgruppe "Kollegium") "Kollegium")))

(defn ordensgruppe-types-sql [ordensgruppe-types]
  (-> 
   (insert-into :public.adressverzeichnis_gruppierungstyp)
   (values (for [ordensgruppe-typ ordensgruppe-types]
              {:name ordensgruppe-typ}))))

(defn ordensgruppen-sql [ordensgruppen]
  (->
   (insert-into :public.adressverzeichnis_gruppierung)
   (values
     (for [{:keys [Ordensgruppe Älterengemeinschaft]} ordensgruppen
           :when (not (str/blank? Ordensgruppe))]
       {:name Ordensgruppe
        :obergruppe_id 
        (when-not (str/blank? Älterengemeinschaft)
          (-> (select :id)
              (from :public.adressverzeichnis_gruppierung)
              (where [:= :name Älterengemeinschaft])))
        :typ_id 
        (when-let [typ (ordensgruppe-typ Ordensgruppe)] 
          (-> (select :id) 
              (from :public.adressverzeichnis_gruppierungstyp) 
              (where [:= :name typ])))}))))

(defn älterengemeinschaften-sql [älterengemeinschaften]
  (-> 
   (insert-into :public.adressverzeichnis_gruppierung)
   (values (for [gemeinschaft älterengemeinschaften
                 :when (not (str/blank? gemeinschaft))]
             {:name gemeinschaft}))))

(defn unmittelbar? 
  ([{:keys [Übergeordnetegruppe Gruppe]}] 
   (= Übergeordnetegruppe Gruppe))
  ([gruppierung gruppierungen]
   (or (unmittelbar? gruppierung)
      (not (contains? (set (map :Gruppe gruppierungen))
                      (:Übergeordnetegruppe gruppierung))))))

(def gruppen-indexer (map #(vector (:Gruppe %) %)))

(defn topo-sort [gruppierungen]
  (let [unmittelbare-gruppen (filter #(unmittelbar? % gruppierungen) gruppierungen)]
    (loop [index (into (ordered-map) gruppen-indexer unmittelbare-gruppen)
           undecided (remove (set unmittelbare-gruppen) gruppierungen)]
      (if (empty? undecided)
        (vals index)
        (let [parents-in-index (filter #(contains? index (:Übergeordnetegruppe %)) undecided)]
          (recur (into index gruppen-indexer parents-in-index)
                 (remove (set parents-in-index) undecided)))))))

(def gruppen-typen 
  #{"Gilde" "Horte" "Trupp"
    "Aufbauhag" "Aufbaustamm"
    "Hag" "Stamm"
    "Mädelschaft" "Jungenschaft"
    "Ring"
    "Gau"})

(defn gruppen-typ [gruppierung]
  (when-let [gruppe (:Gruppe gruppierung)]
    (let [[typ _] (str/split gruppe #"\s")]
      (gruppen-typen typ))))

(defn gruppierungs-typ-sql []
  (-> (insert-into :public.adressverzeichnis_gruppierungstyp)
      (values (for [typ gruppen-typen]
                {:name typ}))))

(defn gruppe-sql [gruppe]
  {:name (:Gruppe gruppe)
   :obergruppe_id
   (when-not (unmittelbar? gruppe)
     (-> (select :id)
         (from :public.adressverzeichnis_gruppierung)
         (where [:= :name (:Übergeordnetegruppe gruppe)])))
   :typ_id
   (when-let [typ (gruppen-typ gruppe)]
     (-> (select :id)
         (from :public.adressverzeichnis_gruppierungstyp)
         (where [:= :name typ])))})

(defn gruppierungen-sql [gruppierungen]
  (let [unmittelbare (filter unmittelbar? gruppierungen)]
    (cons (-> (insert-into :public.adressverzeichnis_gruppierung)
              (values (map gruppe-sql unmittelbare)))
          (for [gruppe (remove unmittelbar? gruppierungen)]
            (->
             (insert-into :public.adressverzeichnis_gruppierung)
             (values [(gruppe-sql gruppe)]))))))

(defn format-sql [sql-map]
  (-> sql-map
   (update :values (fn [values] (map #(assoc % :veraendert "now", :erstellt "now") values)))
   on-conflict do-nothing ; do-update-set
   (sql/format {:inline true, :checking :strict, :pretty true})
   (first)
   (str ";")))

(defn wrap-in-transaction [& x]
  (str (apply str "BEGIN;\n" x) "\nCOMMIT;"))

(print
  (let [persons (map parse-person old)
        gruppierungen (disj (into #{} (map #(select-keys % #{:Übergeordnetegruppe :Gruppe})) persons) {})] 
    (wrap-in-transaction
      (str/join "\n"
        (map format-sql
          (concat
           [(gruppierungs-typ-sql)]
           (gruppierungen-sql (topo-sort gruppierungen))
           (let [ordensgruppen (into #{} (map #(select-keys % #{:Ordensgruppe :Älterengemeinschaft})) persons)]
             [(älterengemeinschaften-sql (set (map :Älterengemeinschaft ordensgruppen)))
              (ordensgruppe-types-sql (disj (set (map ordensgruppe-typ (map :Ordensgruppe ordensgruppen))) nil))
              (ordensgruppen-sql ordensgruppen)])
           [(persons-sql persons)
            (addresses-sql persons)
            (phones-sql persons)]
           (pemissions-sql persons)
           [(amttypen-sql persons)
            (ämter persons)
            (ordensmitgliedschaften-sql persons)]))))))
     