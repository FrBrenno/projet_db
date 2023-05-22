SELECT maladie FROM mydatabase.pathologies 
GROUP BY maladie 
HAVING COUNT(DISTINCT specialite) = 1