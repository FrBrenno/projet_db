SELECT specialite, COUNT(*) 
AS occurences 
FROM diagnostiques 
GROUP BY specialite 
ORDER BY occurences DESC LIMIT 1