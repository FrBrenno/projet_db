def requete1(mycursor):
    # La liste des noms commerciaux de médicaments correspondant à un nom en DCI, classés par ordre alphabétique et taille de conditionnement.
    
    #TODO:Ajouter une option pour pouvoir choisir le DCI qu'on veux (pour l'instant c'est juste ibuprofene)
    dci = "ibuprofene"
    mycursor.execute(
        f"SELECT dci, nom_Commercial, conditionnement FROM medicaments WHERE dci = '{dci}' ORDER BY nom_Commercial ASC, conditionnement ASC")
    res = "1. La liste des noms commerciaux de médicaments correspondant à un nom en DCI, classés par ordre alphabétique et taille de conditionnement.\n\n"
    for x in mycursor:
        res += str(x) + "\n"
    return res


def requete2(mycursor):
    # La liste des pathologies qui peuvent être prise en charge par un seul type de spécialistes.
    mycursor.execute("SELECT maladie FROM pathologies GROUP BY maladie HAVING COUNT(maladie) = 1")        #ici est ce que c'est bien maladie qu'il faut mettre ?
    res = "2. La liste des pathologies qui peuvent être prise en charge par un seul type de spécialistes.\n\n"
    for x in mycursor:
        res += str(x) + "\n"
    return res


def requete3(mycursor):
    # La spécialité de médecins pour laquelle les médecins prescrivent le plus de médicaments.
    mycursor.execute(
        "SELECT specialite, COUNT(*) AS occurences FROM diagnostiques GROUP BY specialite ORDER BY occurences DESC LIMIT 1")
    res = "3. La spécialité de médecins pour laquelle les médecins prescrivent le plus de médicaments.\n\n"
    for x in mycursor:
        res += str(x) + "\n"
    return res

def requete4(mycursor):
    mycursor.execute("")
    res = "4. Tous les utilisateurs ayant consommé un médicament spécifique (sous son nom commercial) après une date donnée, par exemple en cas de rappel de produit pour lot contaminé. \n\n"
    for x in mycursor:
        res += str(x) + "\n"
    return res

def requete5(mycursor):
    mycursor.execute("")
    res = "5. Tous les patients ayant été traités par un médicament (sous sa DCI) à une date antérieure mais qui ne le sont plus, pour vérifier qu’un patients suive bien un traitement chronique.\n\n"
    for x in mycursor:
        res += str(x) + "\n"
    return res

def requete6(mycursor):
    mycursor.execute("")
    res = "6. La liste des médecins ayant prescrit des médicaments ne relevant pas de leur spécialité.\n\n"
    mycursor.execute(
        "SELECT DISTINCT m.nom FROM dossiers_patients dp JOIN medecins m ON m.inami = dp.inami_medecin JOIN medicaments md ON md.dci = dp.dci JOIN specialites s ON s.nom = m.specialite AND s.systeme_anatomique != md.systeme_anatomique")
    for x in mycursor:
        res += str(x) + "\n"
    return res

def requete7(mycursor):
    mycursor.execute("")
    res = "7. Pour chaque décennie entre 1950 et 2020, (1950 − 59, 1960 − 69, ...), le médicament le plus consommé par des patients nés durant cette décennie.\n\n"
    for x in mycursor:
        res += str(x) + "\n"
    return res

def requete8(mycursor):
    mycursor.execute("")
    res = "8. Quelle est la pathologie la plus diagnostiquée ?\n\n"
    for x in mycursor:
        res += str(x) + "\n"
    return res

def requete9(mycursor):
    mycursor.execute("")
    res = "9. Pour chaque patient, le nombre de médecin lui ayant prescrit un médicament.\n\n"
    for x in mycursor:
        res += str(x) + "\n"
    return res

def requete10(mycursor):
    mycursor.execute("")
    res = "10. La liste de médicament n’étant plus prescrit depuis une date spécifique.\n\n"
    for x in mycursor:
        res += str(x) + "\n"
    return res