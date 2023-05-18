import datetime


def requete1(mycursor):
    # La liste des noms commerciaux de médicaments correspondant à un nom en DCI, classés par ordre alphabétique et taille de conditionnement.

    # TODO:Ajouter une option pour pouvoir choisir le DCI qu'on veux (pour l'instant c'est juste ibuprofene)
    dci = "ibuprofene"
    mycursor.execute(
        f"SELECT dci, nom_Commercial, conditionnement FROM medicaments WHERE dci = '{dci}' ORDER BY nom_Commercial ASC, conditionnement ASC")
    res = "1. La liste des noms commerciaux de médicaments correspondant à un nom en DCI, classés par ordre alphabétique et taille de conditionnement.\n\n"
    for x in mycursor:
        res += str(x) + "\n"
    return res


def requete2(mycursor):
    # La liste des pathologies qui peuvent être prise en charge par un seul type de spécialistes.
    mycursor.execute(
        "SELECT maladie FROM pathologies GROUP BY maladie HAVING COUNT(DISTINCT specialite) = 1")
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
    res = "4. Tous les utilisateurs ayant consommé un médicament spécifique (sous son nom commercial) après une date donnée, par exemple en cas de rappel de produit pour lot contaminé. \n\n"
    date = "2001-07-30"
    nom_medicament = "Anfarin"
    res += f"Date : {date}\nNom du médicament : {nom_medicament}\n\n"
    mycursor.execute(
        f"SELECT * FROM patients WHERE NISS IN (SELECT NISS_patient FROM dossiers_patients WHERE date_vente >= '{date}' AND medicament_nom_commercial = '{nom_medicament}')")
    for x in mycursor:
        res += str(x) + "\n"
    return res


def requete5(mycursor):
    res = "5. Tous les patients ayant été traités par un médicament (sous sa DCI) à une date antérieure mais qui ne le sont plus, pour vérifier qu’un patients suive bien un traitement chronique.\n\n"
    dci = "MONTELUKAST"
    mycursor.execute(f"SELECT DISTINCT p.nom, p.prenom FROM patients p JOIN dossiers_patients dp ON p.NISS = dp.NISS_patient WHERE dp.DCI = '{dci}' AND DATEDIFF(CURDATE(), date_vente) < duree_traitement ")
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
    # Brenno
    mycursor.execute("""
        SELECT
        decade,
        MAX(most_consumed_medication) AS most_frequent_medication
        FROM (
            SELECT 
                CONCAT((YEAR(t1.date_de_naissance) DIV 10)*10, '-', (YEAR(t1.date_de_naissance) DIV 10)*10 + 9) AS decade,
                t2.DCI AS most_consumed_medication
            FROM patients t1
            JOIN (
                SELECT
                    p.date_de_naissance,
                    d.DCI,
                    COUNT(*) AS medication_count
                FROM dossiers_patients d
                JOIN patients p ON d.NISS_patient = p.NISS
                GROUP BY p.date_de_naissance, d.DCI
            ) AS t2 ON YEAR(t2.date_de_naissance) >= YEAR(t1.date_de_naissance) DIV 10 * 10
                AND YEAR(t2.date_de_naissance) <= YEAR(t1.date_de_naissance) DIV 10 * 10 + 9
            WHERE YEAR(t1.date_de_naissance) BETWEEN 1950 AND 2020
            GROUP BY decade, most_consumed_medication
        ) AS subquery
        GROUP BY decade
        ORDER BY decade ASC;
    """)
    res = "7. Pour chaque décennie entre 1950 et 2020, (1950 − 59, 1960 − 69, ...), le médicament le plus consommé par des patients nés durant cette décennie.\n\n"
    for x in mycursor:
        res += str(x) + "\n"
    return res


def requete8(mycursor):

    res = "8. Quelle est la pathologie la plus diagnostiquée ?\n\n"
    mycursor.execute("SELECT pathology, COUNT(*) AS diagnosis_count FROM diagnostiques GROUP BY pathology ORDER BY diagnosis_count DESC LIMIT 100")
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
    res = "10. La liste de médicament n’étant plus prescrit depuis une date spécifique.\n\n"
    date = "2001-07-30"
    res += f"Date : {date}\n\n"
    mycursor.execute(f"""
        SELECT DCI
        FROM mydatabase.dossiers_patients dp1
        WHERE NOT EXISTS (
            SELECT 1
            FROM mydatabase.dossiers_patients dp2
            WHERE dp1.DCI = dp2.DCI AND dp2.date_prescription >= '{date}'
        )
    """)
    for x in mycursor:
        res += str(x) + "\n"
    return res


def insert_patient(mycursor, data):
    res = "Insertion d'un patient\n\n"
    mycursor.execute(
        "INSERT INTO patients (NISS, nom, prenom, date_de_naissance, genre, inami_medecin, inami_pharmacien, mail, telephone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
        data)
    for elem in data:
        res += str(elem) + "\n"
    return res


def insert_medecin(mycursor, data):
    res = "Insertion d'un medecin\n\n"
    mycursor.execute(
        "INSERT INTO medecins (inami, nom, specialite, telephone, mail) VALUES (%s, %s, %s, %s, %s)", data)
    for elem in data:
        res += str(elem) + "\n"
    return res


def insert_pharmacien(mycursor, data):
    res = "Insertion d'un pharmacien\n\n"
    mycursor.execute(
        "INSERT INTO pharmaciens (inami, nom, telephone, mail) VALUES (%s, %s, %s, %s)", data)
    for elem in data:
        res += str(elem) + "\n"
    return res
