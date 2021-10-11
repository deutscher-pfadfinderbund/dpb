#!/usr/bin/env bb

(ns migrate
  (:require
   [babashka.deps :as deps]
   [clojure.pprint :as pprint]
   [clojure.string :as str]
   [clojure.set :as set]
   [clojure.java.io :as io])
  (:import java.util.Date))

(deps/add-deps 
 '{:deps 
   {com.github.seancorfield/honeysql {:mvn/version "2.1.818"}
    org.clojure/data.csv {:mvn/version "1.0.0"}}})

(require '[clojure.data.csv :as csv]
         '[honey.sql :as sql]
         '[honey.sql.helpers :as helpers :refer [select insert-into values from where on-conflict do-nothing]])

(def path-to-csv (first *command-line-args*))

(defn csv-data->maps [csv-data]
  (map zipmap
       (->> (first csv-data) ;; First row is the header
            (map keyword) ;; Drop if you want string keys instead
            repeat)
       (rest csv-data)))

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
     :strasse Straße
     :zusatz Zusatz
     :plz Postleitzahl
     :stadt Ort}))

(defn build-number [vorwahl nummer]
  (str vorwahl nummer))

(defn get-numbers [{:keys [Vorwahl1 Telefonnummer1 Telefonbezeichner1
                           Vorwahl2 Telefonnummer2 Telefonbezeichner2
                           Vorwahl3 Telefonnummer3 Telefonbezeichner3]}]
  (let [not-blank? (complement str/blank?)]
    (cond-> []
      (not-blank? Telefonnummer1)
      (conj {:label Telefonbezeichner1
             :nummer (build-number Vorwahl1 Telefonnummer1)})
      
      (not-blank? Telefonnummer2)
      (conj {:label Telefonbezeichner2
             :nummer (build-number Vorwahl2 Telefonnummer2)})
      
      (not-blank? Telefonnummer3)
      (conj {:label Telefonbezeichner3
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
      (update :stand #(get stand-map % ""))))

(defmulti format-value type)
(defmethod format-value String [value]
  (str "'" value "'"))
(defmethod format-value Boolean [value] value)
(defmethod format-value nil [_] "NULL")
#_(defmethod format-value :default [value] (str "ERROR: " value))

(defn adress-sql [address old-id]
  (let [fields (keys address)
        values (map #(format-value (get address %)) fields)]
    (if (every? str/blank? values)
      ""
      (str
       "INSERT INTO public.adressverzeichnis_adresse (" (str/join "," (map name fields)) ",erstellt,veraendert,land,person_id) VALUES ("
       (str/join "," values)
       ",'now','now', 'Deutschland', (SELECT id FROM public.adressverzeichnis_person WHERE adressverzeichnis_person.alte_id = " old-id "));"))))

(defn phone-sql [phone old-id]
  (let [fields (keys phone)
        values (map #(format-value (get phone %)) fields)]
    (str
      "INSERT INTO public.adressverzeichnis_telefon (" (str/join "," (map name fields)) ",erstellt,veraendert,person_id) VALUES ("
      (str/join "," values)
      ",'now','now', (SELECT id FROM public.adressverzeichnis_person WHERE adressverzeichnis_person.alte_id = " old-id "));")))

(defn phones-sql [phones old-id]
  (str/join "\n" (map #(phone-sql % old-id) phones)))

(defn permissions-sql [permissions old-id]
  (let [fields (keys (second (first permissions)))
        values
        (for [[organ-name permission] permissions
              :let [values (map #(format-value (get permission %)) fields)]
              :when (some true? values)]
          (str "(" (str/join "," values) ",'now','now',"
               "(SELECT id FROM public.adressverzeichnis_person WHERE adressverzeichnis_person.alte_id = " old-id "),"
               "(SELECT id FROM public.adressverzeichnis_organ WHERE name = '" organ-name "'))"))]
    (when (seq values)
      (str
       "INSERT INTO public.adressverzeichnis_manuelleberechtigung (" (str/join "," (map name fields)) ", erstellt, veraendert, person_id, organ_id) "
       "VALUES "(str/join ", " values)";"))))

(defn ordensgruppe-mitgliedschaft-sql [ordensgruppe old-id]
  (when-not (str/blank? ordensgruppe)
    (str
      "INSERT INTO public.adressverzeichnis_amt (erstellt, veraendert, bestaetigt, gruppierung_id, person_id, typ_id)
       VALUES ('now', 'now', false, " 
      (str/join ","
        [(str "(SELECT id from public.adressverzeichnis_gruppierung WHERE adressverzeichnis_gruppierung.name = '" ordensgruppe "')")
         (str "(SELECT id from public.adressverzeichnis_person WHERE adressverzeichnis_person.alte_id = " old-id ")")
         (str "(SELECT id from public.adressverzeichnis_amttyp WHERE adressverzeichnis_amttyp.name = 'Mitglied')")])
      ");")))

(defn person-sql [person]
  (let [person (dissoc person :Gruppe :Älterengemeinschaft  :Amt :Ordensamt :Übergeordnetegruppe :Änderungsdatum :Hilfsgruppe)
                      
        fields (keys (dissoc person :address :numbers :permissions :Ordensgruppe))
        old-id (:alte_id person)]
    (str/join "\n"
     [(str "INSERT INTO adressverzeichnis_person (" (str/join "," (map name fields)) ",erstellt, veraendert) VALUES (" (str/join "," (map #(format-value (get person %)) fields)) ",'now','now');")
      (adress-sql (:address person) old-id)
      (phones-sql (:numbers person) old-id)
      (permissions-sql (:permissions person) old-id)
      (ordensgruppe-mitgliedschaft-sql (:Ordensgruppe person) old-id)
      ""])))

(defn ordensgruppe-typ [ordensgruppe]
  (cond
    (str/includes? ordensgruppe "Konvent") "Konvent"
    (str/includes? ordensgruppe "Aufbaukollegium") "Aufbaukollegium"
    (str/includes? ordensgruppe "Kollegium") "Kollegium"))

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
             

(defn format-sql [sql-map]
  (-> sql-map
   (update :values (fn [values] (map #(assoc % :veraendert "now", :erstellt "now") values)))
   on-conflict do-nothing ; do-update-set
   (sql/format {:inline true, :checking :strict})
   (first)
   (str ";")))

(print
  (let [persons (map parse-person old)]
      (str "BEGIN;\n"
        (str/join "\n"
          (concat
            (map format-sql
              (let [ordensgruppen (into #{} (map #(select-keys % #{:Ordensgruppe :Älterengemeinschaft})) persons)]
                [(älterengemeinschaften-sql (set (map :Älterengemeinschaft ordensgruppen)))
                 (ordensgruppe-types-sql (disj (set (map ordensgruppe-typ (map :Ordensgruppe ordensgruppen))) nil))
                 (ordensgruppen-sql ordensgruppen)]))
            (map person-sql persons)))
        "\nCOMMIT;")))