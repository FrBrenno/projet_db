SELECT pathologie, COUNT(*) AS diagnosis_count 
FROM diagnostiques 
GROUP BY pathologie 
ORDER BY diagnosis_count DESC LIMIT 100