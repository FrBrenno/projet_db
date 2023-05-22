SELECT DISTINCT m.nom FROM dossiers_patients dp 
JOIN medecins m ON m.inami = dp.inami_medecin 
JOIN medicaments md ON md.dci = dp.dci 
JOIN specialites s ON s.nom = m.specialite AND s.systeme_anatomique != md.systeme_anatomique
