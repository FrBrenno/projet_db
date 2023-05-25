SELECT p.nom, COUNT(DISTINCT dp.medecin) AS nb
FROM dossiers_patients dp, patients p
WHERE dp.NISS_patient = p.NISS
GROUP BY p.nom
ORDER BY nb