import sys
from CONSTANTS import dico_requêtes

def run_requete(mycursor, num, param = None):
    filename = "../" + f"requetes/requete_{num}.sql" if sys.platform.startswith('win') else f"requetes/requete_{num}.sql"
    res = f"Requête {num} : " + dico_requêtes[num] + "\n\n"

    with open(filename) as f :
        query = " ".join(f.readlines())

    if param != None :
        if type(param) == str :       #Si le paramètre est unique
            mycursor.execute(query, (param,))
        else :
            query = query % param
            mycursor.execute(query)
    else :
        mycursor.execute(query)
    print(query)
    print("OUAIS OUAIS")
    for x in mycursor:
        res += str(x) + "\n"
    return res

def insert_patient(mycursor, data):
    res = "Insertion d'un patient\n\n"
    mycursor.execute(
        "INSERT INTO patients (NISS, nom, prenom, date_de_naissance, genre, inami_medecin, inami_pharmacien, mail, telephone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
        data)
    for elem in data:
        res += str(elem) + "\n"
    return res


def insert_medecin(mycursor, data):
    res = "Insertion d'un medecin\n\n"
    mycursor.execute(
        "INSERT INTO medecins (inami, nom, specialite, telephone, mail) VALUES (%s, %s, %s, %s, %s)", data)
    for elem in data:
        res += str(elem) + "\n"
    return res


def insert_pharmacien(mycursor, data):
    res = "Insertion d'un pharmacien\n\n"
    mycursor.execute(
        "INSERT INTO pharmaciens (inami, nom, telephone, mail) VALUES (%s, %s, %s, %s)", data)
    for elem in data:
        res += str(elem) + "\n"
    return res
