SELECT DISTINCT p.nom, p.prenom 
FROM patients p, dossiers_patients dp 
WHERE p.NISS = dp.NISS_patient 
AND dp.DCI = %s 
AND DATEDIFF(CURDATE(), dp.date_vente) < dp.duree_traitement