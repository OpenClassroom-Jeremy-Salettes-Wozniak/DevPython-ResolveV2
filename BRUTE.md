### Force brute pour générer les portefeuilles d'actions possibles

- Chaque action acheter une seule fois
- 500 € par client max

1. On calcule le calcul du coût de l'action et on ajoute le pourcentage au bout de 2 ans.
2. On liste les actions par ordre de rentabilité (prix + pourcentage).

# On crée une liste qui contient des dictionnaires avec le nom, le prix et le profit de chaque action
actions = [Liste d'actions avec leurs propriétés]

# Importer la bibliothèque "itertools" pour générer des combinaisons
from itertools import combinations

# Importer la bibliothèque "csv" pour la sauvegarde des données
import csv

# Importer la bibliothèque "os" pour la gestion des fichiers
import os

# Fonction pour calculer le profit de chaque action
Fonction calculer_profit(actions):
    Pour chaque action dans les actions:
        Calculer le profit de l'action
    Retourner les actions mises à jour

# Fonction pour créer des portefeuilles d'actions possibles
Fonction create_portefeuille_actions(actions):
    nb_combinaisons_true = 0
    nb_combinaisons_false = 0
    nb_action_min = 1
    nb_action_max = Longueur de la liste des actions

    portefeuille = {
        "name_portefeuille": "",
        "actions": [],
        "profit_total": 0,
    }
    portefeuilles = []

    Pour i allant de nb_action_min à nb_action_max:
        Pour chaque combinaison de i actions parmi les actions:
            Si la somme des prix des actions dans la combinaison est inférieure à 500:
                Incrémenter le nombre de combinaisons valides (nb_combinaisons_true)
                Donner un nom au portefeuille
                Ajouter la combinaison d'actions au portefeuille
                Calculer le profit total du portefeuille
                Ajouter une copie du portefeuille à la liste des portefeuilles
            Sinon:
                Incrémenter le nombre de combinaisons non valides (nb_combinaisons_false)

    Trier les portefeuilles par profit total décroissant

    Sauvegarder les portefeuilles dans un fichier CSV
    Afficher le nombre de combinaisons valides et non valides

# Fonction pour vérifier si la somme des prix des actions est inférieure à 500
Fonction verif_portefeuille(portefeuille):
    Si la somme des prix des actions dans le portefeuille est inférieure ou égale à 500:
        Retourner Vrai
    Sinon:
        Retourner Faux

# Fonction pour sauvegarder les portefeuilles d'actions dans un fichier CSV
Fonction save_portefeuille_actions(portefeuille_actions, nom_fichier):
    Créer un dossier pour stocker les portefeuilles si inexistant
    Créer le chemin du fichier de portefeuilles
    Créer le fichier CSV
    Écrire les données des portefeuilles dans le fichier CSV

# Point d'entrée du programme
Si __name__ est égal à "__main__":
    # On calcule le profit de chaque action individuellement
    actions = calculer_profit(actions)
    
    # On crée les portefeuilles d'actions possibles
    create_portefeuille_actions(actions)
