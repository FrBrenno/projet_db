# Réunion codage 1

Choses à savoir faire au minimum (en python) :

(***DONE***) - Inscrire un nouveau patient, médecin, pharmacien 
- Se connecter en patient pour modif :
  - son med et pharma de référence
  - ses infos medicales
  - Consulter ses traitements
- Fonctionalités en + (optionnelles)

## TO DO

- Un script SQL DDL pour créer la base et les tables
- Script pour importer les données de l'uv. Elles doivent être dedans pour la présentation.

### Requêtes

En alg rel, en calcul tuple et SQL.

1. La liste des noms commerciaux de médicaments correspondant à un nom en DCI, classés par ordre alphabétique et taille de conditionnement. **Brenno** (***DONE***)
2. La liste des pathologies qui peuvent être prise en charge par un seul type de spécialistes. **Alex** (***DONE***)
3. La spécialité de médecins pour laquelle les médecins prescrivent le plus de médicaments. **Philippe** (***DONE***)
4. Tous les utilisateurs ayant consommé un médicament spécifique (sous son nom commercial) après une date donnée, par exemple en cas de rappel de produit pour lot contaminé. (**QUE EN SQL**) **Brenno** (***DONE***)
5. Tous les patients ayant été traités par un médicament (sous sa DCI) à une date antérieure mais qui ne le sont plus, pour vérifier qu’un patients suive bien un traitement chronique. (**QUE EN SQL**) **Alex**
6. La liste des médecins ayant prescrit des médicaments ne relevant pas de leur spécialité. **Philippe** (***DONE***)
7. Pour chaque décennie entre 1950 et 2020, (1950 − 59, 1960 − 69, ...), le médicament le plus consommé par des patients nés durant cette décennie. **Brenno** (***DONE***)
8. Quelle est la pathologie la plus diagnostiquée ? **Alex**
9. Pour chaque patient, le nombre de médecin lui ayant prescrit un médicament. **Philippe**
10. La liste de médicament n’étant plus prescrit depuis une date spécifique. **Le premier qui a fini** (***DONE***)

## Délivrables

- Documents de la 1ere partie (potentiellement modif)
- Slides avec :
  - Méthode extraction des données
  - Requêtes demandées
  - Explication et justif des choix et hypothèses.
- Archive code source :
  - Un fichier dif pour chaque requête
  - Fichier script SQL DDL
  - Script extraction données
