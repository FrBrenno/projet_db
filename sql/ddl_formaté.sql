CREATE TABLE IF NOT EXISTS dossiers_patients 
    (NISS_patient BIGINT, 
    medecin TEXT, 
    inami_medecin BIGINT, 
    pharmacien TEXT, 
    inami_pharmacien BIGINT, 
    medicament_nom_commercial TEXT,
    DCI TEXT, 
    date_prescription DATE, 
    date_vente DATE, 
    duree_traitement INTEGER)
CREATE TABLE IF NOT EXISTS medicaments 
    (dci TEXT, 
    nom_Commercial TEXT, 
    systeme_anatomique TEXT, 
    conditionnement INT)
CREATE TABLE IF NOT EXISTS pathologies 
    (maladie TEXT, specialite TEXT)
CREATE TABLE IF NOT EXISTS medecins 
    (inami BIGINT, 
    nom TEXT, 
    specialite TEXT, 
    telephone BIGINT, 
    mail TEXT)
CREATE TABLE IF NOT EXISTS patients 
    (NISS BIGINT, 
    nom TEXT, 
    prenom TEXT, 
    date_de_naissance DATE, 
    genre INT, 
    inami_medecin BIGINT, 
    inami_pharmacien BIGINT, 
    mail TEXT, 
    telephone BIGINT)
CREATE TABLE IF NOT EXISTS pharmaciens 
    (inami BIGINT, nom TEXT, mail TEXT, telephone BIGINT)
CREATE TABLE IF NOT EXISTS diagnostiques 
    (NISS BIGINT, 
    date_diagnostic DATE, 
    naissance DATE, 
    pathologie TEXT, 
    specialite TEXT)
CREATE TABLE IF NOT EXISTS specialites 
    (nom TEXT, systeme_anatomique TEXT)
-- Doit être représenté ligne par ligne pour fonctionner avec mycursor.execute()