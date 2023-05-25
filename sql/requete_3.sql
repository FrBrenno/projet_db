SELECT m.specialite,
COUNT(*) AS occurences
FROM dossiers_patients dp, medecins m
WHERE dp.inami_medecin = m.inami
GROUP BY m.specialite
ORDER BY occurences DESC LIMIT 100