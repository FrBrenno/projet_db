SELECT medecins.specialite,
COUNT(*) AS occurences
FROM dossiers_patients JOIN medecins
WHERE dossiers_patients.inami_medecin = medecins.inami
GROUP BY medecins.specialite
ORDER BY occurences DESC LIMIT 100
