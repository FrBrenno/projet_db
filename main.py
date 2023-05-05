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

#mycursor.execute("DROP TABLE IF EXISTS dossiers_patients")
#mycursor.execute(
    #"CREATE TABLE dossiers_patients (NISS_patient BIGINT, medecin TEXT, inami_medecin BIGINT, pharmacien TEXT, inami_pharmacien BIGINT, medicament_nom_commercial TEXT, DCI TEXT, date_prescription DATE, date_vente DATE, duree_traitement INTEGER)")

mycursor.execute("INSERT INTO dossiers_patients (NISS_patient, medecin, inami_medecin, pharmacien, inami_pharmacien, medicament_nom_commercial, DCI, date_prescription, date_vente, duree_traitement) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (1, "medecin", 1, "pharmacien", 1, "medicament_nom_commercial", "DCI", "2021-01-01", "2020-02-02", 1))
db.commit()
"""with open("data/dossiers_patients.csv", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        print(row)
        if row[0] != "NISS_patient":
            mycursor.execute(
                "INSERT INTO dossiers_patients (NISS_patient, medecin, inami_medecin, pharmacien, inami_pharmacien, medicament_nom_commercial, DCI, date_prescription, date_vente, duree_traitement) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                row)


"""

