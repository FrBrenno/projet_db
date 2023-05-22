SELECT pathology, COUNT(*) AS diagnosis_count 
FROM diagnostiques 
GROUP BY pathology 
ORDER BY diagnosis_count DESC LIMIT 100