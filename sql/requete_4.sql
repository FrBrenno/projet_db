SELECT * FROM patients 
WHERE NISS IN 
    (SELECT dp.NISS_patient 
    FROM dossiers_patients dp
    WHERE dp.date_vente >= '2001-07-30' 
    AND dp.medicament_nom_commercial = 'Anfarin')