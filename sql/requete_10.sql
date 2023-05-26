SELECT DISTINCT dp1.DCI
FROM dossiers_patients dp1
WHERE dp1.DCI NOT IN(
	SELECT DCI
    FROM dossiers_patients dp2
    WHERE dp2.date_prescription >= %s
)
