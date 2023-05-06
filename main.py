import datetime

import mysql.connector
import xml.etree.ElementTree as ET
import csv


db = mysql.connector.connect(
    host="localhost",
    user="alex",
    passwd="alex",
)

mycursor = db.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
mycursor.execute("USE mydatabase")
#creation des tables


mycursor.execute("CREATE TABLE IF NOT EXISTS dossiers_patients (NISS_patient BIGINT, medecin TEXT, inami_medecin "
                 "BIGINT, pharmacien TEXT, inami_pharmacien BIGINT, medicament_nom_commercial TEXT, DCI TEXT, "
                 "date_prescription DATE, date_vente DATE, duree_traitement INTEGER)")

mycursor.execute("CREATE TABLE IF NOT EXISTS medicaments (dci TEXT,nom_Commercial TEXT,système_anatomique TEXT,"
                 "conditionnement INT)")

mycursor.execute("CREATE TABLE IF NOT EXISTS pathologies (maladie TEXT, systemes TEXT)")

mycursor.execute("CREATE TABLE IF NOT EXISTS medecins (inami BIGINT, nom TEXT, specialite TEXT, telephone BIGINT, mail TEXT)")

mycursor.execute("CREATE TABLE IF NOT EXISTS patients (NISS BIGINT, nom TEXT, prenom TEXT, date_de_naissance DATE, genre INT, inami_medecin BIGINT, inami_pharmacien BIGINT, mail TEXT, telephone BIGINT)")








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


#import des fichiers xml
#import des medecins
tree = ET.parse('data/medecins.xml')
root = tree.getroot()
for medecin in root.findall('medecin'):
    inami = medecin.find('inami').text
    mail = medecin.find('mail').text
    nom = medecin.find('nom').text
    specialite = medecin.find('specialite').text
    telephone = medecin.find('telephone').text
    mycursor.execute("INSERT INTO medecins (inami, nom, specialite, telephone, mail) VALUES (%s, %s, %s, %s, %s)",(inami, nom, specialite, telephone, mail))

#imports des patients
tree = ET.parse('data/patients.xml')
root = tree.getroot()
for patient in root.findall('patient'):
    NISS = patient.find('NISS').text
    nom = patient.find('nom').text
    prenom = patient.find('prenom').text

    date_de_naissance_mauvais_format = patient.find('date_de_naissance').text
    date_de_naissance = datetime.datetime.strptime(date_de_naissance_mauvais_format, "%m/%d/%Y").strftime("%Y-%m-%d")

    genre = patient.find('genre').text
    inami_medecin = patient.find('inami_medecin').text
    inami_pharmacien = patient.find('inami_pharmacien').text
    mail = patient.find('mail').text
    telephone = patient.find('telephone').text
    mycursor.execute("INSERT INTO patients (NISS, nom, prenom, date_de_naissance, genre, inami_medecin, inami_pharmacien, mail, telephone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",(NISS, nom, prenom, date_de_naissance, genre, inami_medecin, inami_pharmacien, mail, telephone))



# Sauvegarder les modifications
db.commit()


