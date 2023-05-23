SELECT NISS_patient, COUNT(*) AS nb
FROM dossiers_patients
GROUP BY NISS_patient
ORDER BY nb