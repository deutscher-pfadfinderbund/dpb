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
   {honeysql/honeysql {:mvn/version "1.0.444"}
    org.clojure/data.csv {:mvn/version "1.0.0"}}})

(require '[clojure.data.csv :as csv]
         '[honeysql.core :as sql]
         '[honeysql.helpers :as helpers])

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
    :bekommt_protokoll (Boolean/parseBoolean (get person (keyword "Protokoll Bundesthing")))}
   "Bundesrat" 
   {:bekommt_einladung (Boolean/parseBoolean Bundesrat)
    :bekommt_protokoll (Boolean/parseBoolean (get person (keyword "Protokoll Bundesrat")))}
   "Bundesmädchenrat" 
   {:bekommt_einladung (Boolean/parseBoolean Bundesmädchenrat)
    :bekommt_protokoll (Boolean/parseBoolean (get person (keyword "Protokoll Bundesmädchenrat")))}
   "Bundesjungenrat" 
   {:bekommt_einladung (Boolean/parseBoolean Bundesjungenrat)
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

(defn person-sql [person]
  (let [person (dissoc person :Gruppe :Älterengemeinschaft :Ordensgruppe :Amt :Ordensamt :Übergeordnetegruppe :Änderungsdatum :Hilfsgruppe
                       :permissions)
        fields (keys (dissoc person :address :numbers))
        old-id (:alte_id person)]
    (str 
     "INSERT INTO adressverzeichnis_person (" (str/join "," (map name fields)) ",erstellt,veraendert) VALUES (" (str/join "," (map #(format-value (get person %)) fields)) ",'now','now');"
     (adress-sql (:address person) old-id)
     (phones-sql (:numbers person) old-id))))

(defn persons-sql [persons]
  (let [persons (map #(dissoc % :Gruppe :ID :Älterengemeinschaft :Ordensgruppe :Amt :Ordensamt :Übergeordnetegruppe :Änderungsdatum :Hilfsgruppe
                              :address :permissions :numbers) persons)]
    []))

(print (str/join "\n" (map (comp person-sql parse-person) old)))