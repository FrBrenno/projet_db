import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="alex",
    passwd="alex",
    database="mydatabase"
)
mycursor = db.cursor()


def requete1():
    mycursor.execute(
        "SELECT dci, nom_Commercial, conditionnement FROM medicaments WHERE dci = 'ibuprofene' ORDER BY nom_Commercial ASC, conditionnement ASC")
    for x in mycursor:
        print(x)

def requete2():
    # La liste des pathologies qui peuvent être prise en charge par un seul type de spécialistes.
    mycursor.execute("SELECT maladie FROM pathologies GROUP BY maladie HAVING COUNT(maladie) = 1")
    for x in mycursor:
        print(x)





#requete1()
requete2()