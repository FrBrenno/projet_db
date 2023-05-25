SELECT DISTINCT m.nom FROM dossiers_patients dp 
JOIN medecins m ON m.inami = dp.inami_medecin 
JOIN medicaments md ON md.dci = dp.dci 
JOIN specialites s ON s.nom = m.specialite AND s.systeme_anatomique != md.systeme_anatomique

-- SELECT DISTINCT m.nom FROM medecins m, dossiers_patients dp, medicaments md, specialites s
-- WHERE m.inami = dp.inami_medecin
-- AND WHERE md.DCI = dp.DCI
-- AND WHERE s.specialite = m.specialite AND s.systeme_anatomique != md.systeme_anatomique
