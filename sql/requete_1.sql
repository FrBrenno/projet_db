SELECT dci, nom_Commercial, conditionnement FROM medicaments 
WHERE dci = %s
ORDER BY nom_Commercial ASC, conditionnement ASC