CREATE TABLE IF NOT EXISTS medicaments (
    dci TEXT,
    nom_Commercial TEXT,
    systeme_anatomique TEXT,
    conditionnement INT,
    PRIMARY KEY (dci(255),
    nom_Commercial(255),
    conditionnement)
);
CREATE TABLE IF NOT EXISTS pathologies (
    maladie TEXT,
    specialite TEXT,
    PRIMARY KEY (maladie(255), specialite(255))
);
CREATE TABLE IF NOT EXISTS medecins (
    inami BIGINT PRIMARY KEY ,
    nom TEXT,
    specialite TEXT,
    telephone BIGINT,
    mail TEXT
);
CREATE TABLE IF NOT EXISTS patients (
    NISS BIGINT PRIMARY KEY ,
    nom TEXT, prenom TEXT,
    date_de_naissance DATE,
    genre INT,
    inami_medecin BIGINT,
    inami_pharmacien BIGINT,
    mail TEXT,
    telephone BIGINT
);
CREATE TABLE IF NOT EXISTS pharmaciens (
    inami BIGINT PRIMARY KEY ,
    nom TEXT,
    mail TEXT,
    telephone BIGINT
);
CREATE TABLE IF NOT EXISTS diagnostiques (
    NISS BIGINT,
    date_diagnostic DATE,
    naissance DATE,
    pathologie TEXT,
    specialite TEXT,
    PRIMARY KEY (NISS, date_diagnostic, pathologie(255))
);
CREATE TABLE IF NOT EXISTS specialites (
    nom TEXT,
    systeme_anatomique TEXT,
    PRIMARY KEY (nom(255), systeme_anatomique(255))
);
CREATE TABLE IF NOT EXISTS dossiers_patients (
    NISS_patient BIGINT,
    medecin TEXT,
    inami_medecin BIGINT,
    pharmacien TEXT,
    inami_pharmacien BIGINT,
    medicament_nom_commercial TEXT(255),
    DCI TEXT(255), date_prescription DATE,
    date_vente DATE,
    duree_traitement INTEGER,
    PRIMARY KEY (NISS_patient, medicament_nom_commercial(255), date_prescription),
    FOREIGN KEY (NISS_patient) REFERENCES patients(NISS),
    FOREIGN KEY (medecin(255)) REFERENCES medecins(nom),
    FOREIGN KEY (inami_medecin) REFERENCES medecins(inami),
    FOREIGN KEY (pharmacien(255)) REFERENCES pharmaciens(nom),
    FOREIGN KEY (inami_pharmacien) REFERENCES pharmaciens(inami),
    FOREIGN KEY (medicament_nom_commercial(255)) REFERENCES medicaments(nom_Commercial),
    FOREIGN KEY (DCI(255)) REFERENCES medicaments(dci)
);
