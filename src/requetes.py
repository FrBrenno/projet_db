import datetime
import sys
from CONSTANTS import dico_requêtes, dico_fichiers_requete

def run_requete(mycursor, num, param = None):
    filename = dico_fichiers_requete[num]
    filename = "../" + filename if sys.platform.startswith('win') else filename
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
        print(x)
        x = list(x)
        for i, y in enumerate(x):
            if type(y) == datetime.date :
                x[i] = y.strftime("%d/%m/%Y") + " "
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


def requet_voir_info_medical(mycursor, NISS):
    mycursor.execute("SELECT date_diagnostic, pathologie, specialite FROM diagnostiques WHERE NISS = %s", (NISS,))
    res = []
    for x in mycursor:
        x = list(x)
        x[0] = x[0].strftime("%d/%m/%Y")
        res.append(str(x) + "\n")
    print(res)
    return res

def requet_voir_traitements(mycursor, NISS):
    mycursor.execute("SELECT medecin, inami_medecin, pharmacien, inami_pharmacien, medicament_nom_commercial, DCI, date_prescription, date_vente, duree_traitement FROM dossiers_patients WHERE NISS_patient = %s", (NISS,))
    res = []
    for x in mycursor:
        x = list(x)
        x[6] = x[6].strftime("%d/%m/%Y")
        x[7] = x[7].strftime("%d/%m/%Y")
        res.append(str(x) + "\n")
    return res