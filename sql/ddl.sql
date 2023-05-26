CREATE TABLE IF NOT EXISTS specialites (
    nom VARCHAR(255),
    systeme_anatomique VARCHAR(255),
    PRIMARY KEY (nom, systeme_anatomique)
);
CREATE TABLE IF NOT EXISTS pharmaciens (
    inami BIGINT PRIMARY KEY,
    nom VARCHAR(255),
    mail VARCHAR(255),
    telephone BIGINT
);
CREATE TABLE  medecins (
    inami BIGINT PRIMARY KEY ,
    nom VARCHAR(255),
    specialite VARCHAR(255),
    telephone BIGINT,
    mail VARCHAR(255),
    FOREIGN KEY (specialite) REFERENCES specialites(nom)
);
CREATE TABLE  medicaments (
    dci VARCHAR(255),
    nom_Commercial VARCHAR(255),
    systeme_anatomique VARCHAR(255),
    conditionnement INT,
    PRIMARY KEY (dci, nom_Commercial, conditionnement)
);
CREATE TABLE IF NOT EXISTS patients (
    NISS BIGINT PRIMARY KEY ,
    nom VARCHAR(255), prenom VARCHAR(255),
    date_de_naissance DATE,
    genre INT,
    inami_medecin BIGINT,
    inami_pharmacien BIGINT,
    mail VARCHAR(255),
    telephone BIGINT,
    FOREIGN KEY (inami_medecin) REFERENCES medecins(inami),
    FOREIGN KEY (inami_pharmacien) REFERENCES pharmaciens(inami)
);
CREATE TABLE IF NOT EXISTS pathologies (
    maladie VARCHAR(255),
    specialite VARCHAR(255),
    PRIMARY KEY (maladie, specialite)
);
CREATE TABLE IF NOT EXISTS diagnostiques (
    NISS BIGINT,
    date_diagnostic DATE,
    naissance DATE,
    pathologie VARCHAR(255),
    specialite VARCHAR(255),
    PRIMARY KEY (NISS, date_diagnostic, pathologie(255))
);
CREATE TABLE IF NOT EXISTS dossiers_patients (
    NISS_patient BIGINT,
    medecin VARCHAR(255),
    inami_medecin BIGINT,
    pharmacien VARCHAR(255),
    inami_pharmacien BIGINT,
    medicament_nom_commercial VARCHAR(255),
    DCI VARCHAR(255), date_prescription DATE,
    date_vente DATE,
    duree_traitement INTEGER,
    FOREIGN KEY (NISS_patient) REFERENCES patients(NISS),
    FOREIGN KEY (inami_medecin) REFERENCES medecins(inami),
    FOREIGN KEY (inami_pharmacien) REFERENCES pharmaciens(inami),
    FOREIGN KEY (DCI) REFERENCES medicaments(dci)
);
