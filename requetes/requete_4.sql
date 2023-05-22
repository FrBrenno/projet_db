SELECT * FROM patients 
WHERE NISS IN 
    (SELECT NISS_patient 
    FROM dossiers_patients 
    WHERE date_vente >= '2001-07-30' 
    AND medicament_nom_commercial = 'Anfarin')