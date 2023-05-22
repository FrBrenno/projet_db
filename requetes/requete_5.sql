SELECT DISTINCT p.nom, p.prenom 
FROM patients p 
JOIN dossiers_patients dp 
ON p.NISS = dp.NISS_patient 
WHERE dp.DCI = 'MONTELUKAST' AND DATEDIFF(CURDATE(), date_vente) < duree_traitement