import sys

nom = ""

DOSSIER_PATIENT_CSV = "data/dossiers_patients.csv"
MEDICAMENT_CSV = "data/medicaments.csv"
PHATOLOGIES_CSV = "data/pathologies.csv"
MEDECINS_XML = 'data/medecins.xml'
PATIENTS_XML = 'data/patients.xml'
PHARMACIENS_XML = 'data/pharmaciens.xml'
DIAGNOSTIQUES_XML = 'data/diagnostiques.xml'
SPECIALITES_XML = 'data/specialites.xml'

if nom == "La plèbe":
    DOSSIER_PATIENT_CSV = "../" + DOSSIER_PATIENT_CSV
    MEDICAMENT_CSV = "../" + MEDICAMENT_CSV
    PHATOLOGIES_CSV = "../" + PHATOLOGIES_CSV
    MEDECINS_XML = '../' + MEDECINS_XML
    PATIENTS_XML = '../' + PATIENTS_XML
    PHARMACIENS_XML = '../' + PHARMACIENS_XML
    DIAGNOSTIQUES_XML = '../' + DIAGNOSTIQUES_XML
    SPECIALITES_XML = '../' + SPECIALITES_XML
