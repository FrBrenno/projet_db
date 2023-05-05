import datetime

import mysql.connector
import csv


db = mysql.connector.connect(
    host="localhost",
    user="alex",
    passwd="alex",
    database="mydatabase"
)

mycursor = db.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")

#creation des tables


mycursor.execute("CREATE TABLE IF NOT EXISTS dossiers_patients (NISS_patient BIGINT, medecin TEXT, inami_medecin "
                 "BIGINT, pharmacien TEXT, inami_pharmacien BIGINT, medicament_nom_commercial TEXT, DCI TEXT, "
                 "date_prescription DATE, date_vente DATE, duree_traitement INTEGER)")

mycursor.execute("CREATE TABLE IF NOT EXISTS medicaments (dci TEXT,nom_Commercial TEXT,système_anatomique TEXT,"
                 "conditionnement INT)")

mycursor.execute("CREATE TABLE IF NOT EXISTS pathologies (maladie TEXT, systemes TEXT)")

# enlève les données des tables si elles existent déjà
mycursor.execute("DELETE FROM dossiers_patients")
mycursor.execute("DELETE FROM medicaments")
mycursor.execute("DELETE FROM pathologies")

# insertion des données dans les tables


with open("data/dossiers_patients.csv", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:

        if row[0] != "NISS_patient":

            # convertir les dates mois/jour/annee au format date annee-mois-jour
            date_prescription_mauvais_format = row[7]
            date_obj_prescri = datetime.datetime.strptime(date_prescription_mauvais_format, "%m/%d/%Y")
            row[7] = date_obj_prescri.strftime("%Y-%m-%d")

            date_vente_mauvais_format = row[8]
            date_obj_vente = datetime.datetime.strptime(date_vente_mauvais_format, "%m/%d/%Y")
            row[8] = date_obj_prescri.strftime("%Y-%m-%d")


            mycursor.execute("INSERT INTO dossiers_patients (NISS_patient, medecin, inami_medecin, pharmacien, inami_pharmacien, medicament_nom_commercial, DCI, date_prescription, date_vente, duree_traitement) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",row)


with open("data/medicaments.csv", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        if row[0] != "dci":

            mycursor.execute("INSERT INTO medicaments (dci, nom_Commercial, système_anatomique, conditionnement) VALUES (%s, %s, %s, %s)",row)


with open("data/pathologies.csv", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        if row[0] != "maladie":

            mycursor.execute(
                "INSERT INTO pathologies (maladie, systemes) VALUES (%s, %s)",
                row)


# Sauvegarder les modifications
db.commit()


