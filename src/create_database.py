import mysql.connector




def create_database(mydb):
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
    mycursor.execute("USE mydatabase")
    # creation des tables
    create_tables(mycursor)
    # enlève les données des tables si elles existent déjà
    clear_data(mycursor)


def clear_data(mycursor):
    mycursor.execute("DELETE FROM dossiers_patients")
    mycursor.execute("DELETE FROM medicaments")
    mycursor.execute("DELETE FROM pathologies")
    mycursor.execute("DELETE FROM medecins")
    mycursor.execute("DELETE FROM patients")
    mycursor.execute("DELETE FROM pharmaciens")
    mycursor.execute("DELETE FROM diagnostiques")
    mycursor.execute("DELETE FROM specialites")


def create_tables(mycursor):
    mycursor.execute("CREATE TABLE IF NOT EXISTS dossiers_patients (NISS_patient BIGINT, medecin TEXT, inami_medecin "
                     "BIGINT, pharmacien TEXT, inami_pharmacien BIGINT, medicament_nom_commercial TEXT, DCI TEXT, "
                     "date_prescription DATE, date_vente DATE, duree_traitement INTEGER)")
    mycursor.execute("CREATE TABLE IF NOT EXISTS medicaments (dci TEXT,nom_Commercial TEXT,systeme_anatomique TEXT,"
                     "conditionnement INT)")
    mycursor.execute("CREATE TABLE IF NOT EXISTS pathologies (maladie TEXT, specialite TEXT)")
    mycursor.execute(
        "CREATE TABLE IF NOT EXISTS medecins (inami BIGINT, nom TEXT, specialite TEXT, telephone BIGINT, mail TEXT)")
    mycursor.execute(
        "CREATE TABLE IF NOT EXISTS patients (NISS BIGINT, nom TEXT, prenom TEXT, date_de_naissance DATE, genre INT, inami_medecin BIGINT, inami_pharmacien BIGINT, mail TEXT, telephone BIGINT)")
    mycursor.execute("CREATE TABLE IF NOT EXISTS pharmaciens (inami BIGINT, nom TEXT, mail TEXT, telephone BIGINT)")
    mycursor.execute(
        "CREATE TABLE IF NOT EXISTS diagnostiques (NISS BIGINT, date_diagnostic DATE, naissance DATE, pathology TEXT, specialite TEXT)")
    mycursor.execute(
        "CREATE TABLE IF NOT EXISTS specialites (nom TEXT, systeme_anatomique TEXT)")


