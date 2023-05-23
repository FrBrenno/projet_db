DOSSIER_PATIENT_CSV = "data/dossiers_patients.csv"
MEDICAMENT_CSV = "data/medicaments.csv"
PHATOLOGIES_CSV = "data/pathologies.csv"
MEDECINS_XML = 'data/medecins.xml'
PATIENTS_XML = 'data/patients.xml'
PHARMACIENS_XML = 'data/pharmaciens.xml'
DIAGNOSTIQUES_XML = 'data/diagnostiques.xml'
SPECIALITES_XML = 'data/specialites.xml'

dico_requêtes = {1: "La liste des noms commerciaux de médicaments correspondant à un nom en DCI, classés par ordre alphabétique et taille de conditionnement",
                 2: "La liste des pathologies qui peuvent être prise en charge par un seul type de spécialistes.",
                 3: "La spécialité de médecins pour laquelle les médecins prescrivent le plus de médicaments.",
                 4: "Tous les utilisateurs ayant consommé un médicament spécifique (sous son nom commercial) après une date donnée, par exemple en cas de rappel de produit pour lot contaminé.",
                 5 : "Tous les patients ayant été traités par un médicament (sous sa DCI) à une date antérieure mais qui ne le sont plus, pour vérifier qu’un patients suive bien un traitement chronique.",
                 6 : "La liste des médecins ayant prescrit des médicaments ne relevant pas de leur spécialité.",
                 7 : "Pour chaque décennie entre 1950 et 2020, (1950 - 59, 1960 - 69, ...), le médicament le plus consommé par des patients nés durant cette décennie.",
                 8 : "Quelle est la pathologie la plus diagnostiquée ?",
                 9 : "Pour chaque patient, le nombre de médecin lui ayant prescrit un médicament.",
                 10 : "La liste de médicament n’étant plus prescrit depuis une date spécifique."}