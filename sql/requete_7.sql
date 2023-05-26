SELECT 
	decade, 
    most_consumed_medication
FROM (
  SELECT 
    CONCAT((YEAR(p.date_de_naissance) DIV 10)*10, '-', (YEAR(p.date_de_naissance) DIV 10)*10 + 9) AS decade,
    d.DCI AS most_consumed_medication,
    ROW_NUMBER() OVER (PARTITION BY CONCAT((YEAR(p.date_de_naissance) DIV 10)*10, '-', (YEAR(p.date_de_naissance) DIV 10)*10 + 9) ORDER BY COUNT(*) DESC) AS rn
  FROM dossiers_patients d
  JOIN patients p ON d.NISS_patient = p.NISS
  WHERE YEAR(p.date_de_naissance) BETWEEN 1950 AND 2020
  GROUP BY CONCAT((YEAR(p.date_de_naissance) DIV 10)*10, '-', (YEAR(p.date_de_naissance) DIV 10)*10 + 9), d.DCI
) as subquery
WHERE rn = 1
GROUP BY decade, most_consumed_medication
ORDER BY decade ASC;
