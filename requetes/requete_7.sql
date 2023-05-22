SELECT
decade,
MAX(most_consumed_medication) AS most_frequent_medication
FROM (
    SELECT 
        CONCAT((YEAR(t1.date_de_naissance) DIV 10)*10, '-', (YEAR(t1.date_de_naissance) DIV 10)*10 + 9) AS decade,
        t2.DCI AS most_consumed_medication
    FROM patients t1
    JOIN (
        SELECT
            p.date_de_naissance,
            d.DCI,
            COUNT(*) AS medication_count
        FROM dossiers_patients d
        JOIN patients p ON d.NISS_patient = p.NISS
        GROUP BY p.date_de_naissance, d.DCI
    ) AS t2 ON YEAR(t2.date_de_naissance) >= YEAR(t1.date_de_naissance) DIV 10 * 10
        AND YEAR(t2.date_de_naissance) <= YEAR(t1.date_de_naissance) DIV 10 * 10 + 9
    WHERE YEAR(t1.date_de_naissance) BETWEEN 1950 AND 2020
    GROUP BY decade, most_consumed_medication
) AS subquery
GROUP BY decade
ORDER BY decade ASC;