SELECT maladie FROM pathologies
GROUP BY maladie 
HAVING COUNT(DISTINCT specialite) = 1