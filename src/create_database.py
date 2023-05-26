from CONSTANTS import FICHIER_DDL
import sys

def create_database(mydb):
    print("CREATING DATABASE")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
    mycursor.execute("USE mydatabase")
    # creation des tables
    create_tables(mycursor, mydb)
    # enlève les données des tables si elles existent déjà
    #clear_data(mycursor)


def clear_data(mycursor):
    mycursor.execute("DELETE FROM medicaments")
    mycursor.execute("DELETE FROM pathologies")
    mycursor.execute("DELETE FROM medecins")
    mycursor.execute("DELETE FROM patients")
    mycursor.execute("DELETE FROM pharmaciens")
    mycursor.execute("DELETE FROM diagnostiques")
    mycursor.execute("DELETE FROM specialites")
    mycursor.execute("DELETE FROM dossiers_patients")


def create_tables(mycursor, db):
    print("CREATING TABLES")
    with open(FICHIER_DDL, "r") as f:
        commande = ""
        for line in f:
            print(line)
            if line.startswith("CREATE TABLE"):
                commande = ""
            if line.endswith(";\n"):
                commande += line
                print(commande)
                mycursor.execute(commande)
                db.commit()

                commande = ""
            else:
                commande += line
