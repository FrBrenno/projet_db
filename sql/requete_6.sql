SELECT DISTINCT m.nom FROM medecins m, dossiers_patients dp, medicaments md, specialites s
WHERE m.inami = dp.inami_medecin
AND md.DCI = dp.DCI
AND s.nom = m.specialite
AND s.systeme_anatomique != md.systeme_anatomique
