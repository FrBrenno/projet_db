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


def requet_check_NISS(mycursor, NISS):
    mycursor.execute("SELECT * FROM patients WHERE NISS = %s", (NISS,))
    res = mycursor.fetchall()
    if len(res) == 0:
        return False
    else:
        return True


def requet_check_inami_medecin(mycursor, inami):
    mycursor.execute("SELECT * FROM medecins WHERE inami = %s", (inami,))
    res = mycursor.fetchall()
    if len(res) == 0:
        return False
    else:
        return True


def requet_check_inami_pharmacien(mycursor, inami):
    mycursor.execute("SELECT * FROM pharmaciens WHERE inami = %s", (inami,))
    res = mycursor.fetchall()
    if len(res) == 0:
        return False
    else:
        return True


def requet_info_patient(mycursor, NISS):
    mycursor.execute("SELECT DISTINCT * FROM patients WHERE NISS = %s", (NISS,))
    #renvoie un tuple des infos du patient
    res = mycursor.fetchall()

    return list(res[0])


def requet_changer_medecin(mycursor, NISS, inami_medecin):
    mycursor.execute("UPDATE patients SET inami_medecin = %s WHERE NISS = %s", (inami_medecin, NISS))
    return True


def requete_changer_pharmacien(mycursor, NISS, inami_pharmacien):
    mycursor.execute("UPDATE patients SET inami_pharmacien = %s WHERE NISS = %s", (inami_pharmacien, NISS))
    return True