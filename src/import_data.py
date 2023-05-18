import csv
import datetime
import xml.etree.ElementTree as ElemTree

from CONSTANTS import *


def convert_data_format(date_wrong_format):
    """
    Convertit une date du format mois/jour/annee au format annee-mois-jour
    :param date_wrong_format:
    :return:
    """
    date_obj = datetime.datetime.strptime(date_wrong_format, "%m/%d/%Y")
    date = date_obj.strftime("%Y-%m-%d")
    return date


# insertion des données dans les tables

def import_data(mydb, os_name):
    """
    Importe les données des fichiers csv et xml dans la base de données
    :param mydb: mysql database connection
    """
    mycursor = mydb.cursor()
    mycursor.execute("USE mydatabase")
    OPERATING_SYSTEM = os_name

    import_csv_data(mycursor, OPERATING_SYSTEM)
    import_xml_data(mycursor, OPERATING_SYSTEM)
    # Sauvegarder les modifications
    mydb.commit()


def import_csv_data(mycursor, os):
    DOSSIER_PATIENT_CSV_PATH = "../" + DOSSIER_PATIENT_CSV if os == "Windows" else DOSSIER_PATIENT_CSV
    MEDICAMENT_CSV_PATH = "../" + MEDICAMENT_CSV if os == "Windows" else MEDICAMENT_CSV
    PHATOLOGIES_CSV_PATH = "../" + PHATOLOGIES_CSV if os == "Windows" else PHATOLOGIES_CSV

    import_dossier_patient_csv(DOSSIER_PATIENT_CSV_PATH, mycursor)
    import_medicament_csv(MEDICAMENT_CSV_PATH, mycursor)
    import_phatologies_csv(PHATOLOGIES_CSV_PATH, mycursor)


def import_phatologies_csv(PHATOLOGIES_CSV_PATH, mycursor):
    with open(PHATOLOGIES_CSV_PATH, encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            if row[0] != "maladie":
                # vérifie que la maladie n'est pas déjà dans la base de données avec le même système anatomique
                mycursor.execute("SELECT * FROM pathologies WHERE maladie = %s AND specialite = %s", (row[0], row[1]))
                result = mycursor.fetchall()
                if len(result) == 0:
                    mycursor.execute(
                        "INSERT INTO pathologies (maladie, specialite) VALUES (%s, %s)",
                        row)


def import_medicament_csv(MEDICAMENT_CSV_PATH, mycursor):
    with open(MEDICAMENT_CSV_PATH, encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            if row[0] != "dci":
                mycursor.execute("INSERT INTO medicaments (dci, nom_Commercial, systeme_anatomique, conditionnement) "
                                 "VALUES (%s, %s, %s, %s)", row)


def import_dossier_patient_csv(DOSSIER_PATIENT_CSV_PATH, mycursor):
    with open(DOSSIER_PATIENT_CSV_PATH, encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            if row[0] != "NISS_patient":
                # convertir les dates mois/jour/annee au format date annee-mois-jour
                date_prescription_mauvais_format = row[7]
                row[7] = convert_data_format(date_prescription_mauvais_format)
                date_vente_mauvais_format = row[8]
                row[8] = convert_data_format(date_vente_mauvais_format)
                mycursor.execute("INSERT INTO dossiers_patients (NISS_patient, medecin, inami_medecin, pharmacien, "
                                 "inami_pharmacien, medicament_nom_commercial, DCI, date_prescription, date_vente, "
                                 "duree_traitement) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", row)


def import_xml_data(mycursor, os):
    MEDECINS_XML_PATH = "../" + MEDECINS_XML if os == "Windows" else MEDECINS_XML
    PATIENTS_XML_PATH = "../" + PATIENTS_XML if os == "Windows" else PATIENTS_XML
    PHARMACIENS_XML_PATH = "../" + PHARMACIENS_XML if os == "Windows" else PHARMACIENS_XML
    DIAGNOSTIQUES_XML_PATH = "../" + DIAGNOSTIQUES_XML if os == "Windows" else DIAGNOSTIQUES_XML
    SPECIALITES_XML_PATH = "../" + SPECIALITES_XML if os == "Windows" else SPECIALITES_XML

    import_medecin_xml(MEDECINS_XML_PATH, mycursor)
    import_patient_xml(PATIENTS_XML_PATH, mycursor)
    import_pharmacien_xml(PHARMACIENS_XML_PATH, mycursor)
    import_diagnostique_xml(DIAGNOSTIQUES_XML_PATH, mycursor)
    import_specialite_xml(SPECIALITES_XML_PATH, mycursor)


def import_specialite_xml(SPECIALITES_XML_PATH, mycursor):
    tree = ElemTree.parse(SPECIALITES_XML_PATH)
    root = tree.getroot()
    for specialite in root.findall('specialite'):
        nom = specialite.find('name').text
        for systeme_anat in specialite.findall('medicament'):
            systeme_anat = systeme_anat.text
            mycursor.execute("INSERT INTO specialites (nom, systeme_anatomique) VALUES (%s, %s)",
                             (nom, systeme_anat))


def import_diagnostique_xml(DIAGNOSTIQUES_XML_PATH, mycursor):
    tree = ElemTree.parse(DIAGNOSTIQUES_XML_PATH)
    root = tree.getroot()
    for diagnostic in root.findall('diagnostique'):
        NISS = diagnostic.find('NISS').text

        date_diagnostic_mauvais_format = diagnostic.find('date_diagnostic').text
        date_diagnostic = convert_data_format(date_diagnostic_mauvais_format)

        naissance_mauvais_format = diagnostic.find('naissance').text
        naissance = convert_data_format(naissance_mauvais_format)

        pathology = diagnostic.find('pathology').text
        specialite = diagnostic.find('specialite').text
        if specialite == " Dermatologie et vénérologie":
            specialite = "Dermatologie et vénérologie"
        elif specialite == " Gynécologie médicale":
            specialite = "Gynécologie médicale"
        mycursor.execute(
            "INSERT INTO diagnostiques (NISS, date_diagnostic, naissance, pathology, specialite) VALUES (%s, %s, %s, %s, %s)",
            (NISS, date_diagnostic, naissance, pathology, specialite))


def import_pharmacien_xml(PHARMACIENS_XML_PATH, mycursor):
    tree = ElemTree.parse(PHARMACIENS_XML_PATH)
    root = tree.getroot()
    for pharmacien in root.findall('pharmacien'):
        inami = pharmacien.find('inami').text
        mail = pharmacien.find('mail').text
        nom = pharmacien.find('nom').text
        telephone = pharmacien.find('tel').text
        mycursor.execute("INSERT INTO pharmaciens (inami, nom, mail, telephone) VALUES (%s, %s, %s, %s)",
                         (inami, nom, mail, telephone))


def import_patient_xml(PATIENTS_XML_PATH, mycursor):
    tree = ElemTree.parse(PATIENTS_XML_PATH)
    root = tree.getroot()
    for patient in root.findall('patient'):
        NISS = patient.find('NISS').text
        nom = patient.find('nom').text
        prenom = patient.find('prenom').text

        date_de_naissance_mauvais_format = patient.find('date_de_naissance').text
        date_de_naissance = convert_data_format(date_de_naissance_mauvais_format)

        genre = patient.find('genre').text
        inami_medecin = patient.find('inami_medecin').text
        inami_pharmacien = patient.find('inami_pharmacien').text
        mail = patient.find('mail').text
        telephone = patient.find('telephone').text
        mycursor.execute(
            "INSERT INTO patients (NISS, nom, prenom, date_de_naissance, genre, inami_medecin, inami_pharmacien, mail, telephone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (NISS, nom, prenom, date_de_naissance, genre, inami_medecin, inami_pharmacien, mail, telephone))


def import_medecin_xml(MEDECINS_XML_PATH, mycursor):
    tree = ElemTree.parse(MEDECINS_XML_PATH)
    root = tree.getroot()
    for medecin in root.findall('medecin'):
        inami = medecin.find('inami').text
        mail = medecin.find('mail').text
        nom = medecin.find('nom').text
        specialite = medecin.find('specialite').text
        telephone = medecin.find('telephone').text
        mycursor.execute("INSERT INTO medecins (inami, nom, specialite, telephone, mail) VALUES (%s, %s, %s, %s, %s)",
                         (inami, nom, specialite, telephone, mail))
