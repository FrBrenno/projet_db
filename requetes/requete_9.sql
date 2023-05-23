SELECT p.nom, COUNT(medecin) AS nb
FROM dossiers_patients d, patients p
WHERE d.NISS_patient = p.NISS
GROUP BY p.nom
ORDER BY nb