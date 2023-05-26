SELECT DISTINCT DCI
FROM mydatabase.dossiers_patients dp1
WHERE DCI NOT IN(
	SELECT DCI
    FROM mydatabase.dossiers_patients dp2
    WHERE dp1.DCI = dp2.DCI AND dp2.date_prescription >= '2001-07-30'
)
