# Chaque action acheter une seul fois
# C'est donc une action complete int
# 500 € par client max

# 1. On calcule le calcul du coup de l'action et on ajoute le pourcentage au bout de 2ans
# 2. On la liste des actions par ordre de rentabilité (prix + pourcentage)

# On créer une liste qui contient des dictionsnaire avec le name,price,profit de chaque action
actions = [
    {
        "name": "action1",
        "price": 20,
        "profit": 5
    },
    {
        "name": "action2",
        "price": 30,
        "profit": 10
    },
    {
        "name": "action3",
        "price": 50,
        "profit": 15
    },
    {
        "name": "action4",
        "price": 70,
        "profit": 20
    },
    {
        "name": "action5",
        "price": 60,
        "profit": 17
    },
    {
        "name": "action6",
        "price": 80,
        "profit": 25
    },
    {
        "name": "action7",
        "price": 22,
        "profit": 7
    },
    {
        "name": "action8",
        "price": 26,
        "profit": 11
    },
    {
        "name": "action9",
        "price": 48,
        "profit": 13
    },
    {
        "name": "action10",
        "price": 34,
        "profit": 27
    },
    {
        "name": "action11",
        "price": 42,
        "profit": 17
    },
    {
        "name": "action12",
        "price": 110,
        "profit": 9
    },
    {
        "name": "action13",
        "price": 38,
        "profit": 23
    },
    {
        "name": "action14",
        "price": 14,
        "profit": 1
    },
    {
        "name": "action15",
        "price": 18,
        "profit": 3
    },
    {
        "name": "action16",
        "price": 8,
        "profit": 8
    },
    {
        "name": "action17",
        "price": 4,
        "profit": 12
    },
    {
        "name": "action18",
        "price": 10,
        "profit": 14
    },
    {
        "name": "action19",
        "price": 24,
        "profit": 21
    },
    {
        "name": "action20",
        "price": 114,
        "profit": 18
    },
]

from itertools import combinations
import csv
import os
# Créer plusieurs portefeuille d'action qui propose des actions avec pour limite 500 et une dont une seul action est achetable
# Pour cela il faudra permuter les actions et créer les listes d'actions.
def calcul_profit(actions):
    # On calcul le profit de chaque action
    for action in actions:
        # On calcul le profit de chaque action
        action["profit"] =  action["price"] * action["profit"] / 100
    return actions

def create_portefeuille_actions(actions):
    # On créer une liste de toutes les combinaisons possibles limite 500 et une dont une seul action est achetable
    nb_combinaisons_true = 0
    nb_combinaisons_false = 0
    nb_action_min = 1
    nb_action_max = len(actions)
    portefeuille = {
        "name_portefeuille": "",
        "actions": [],
        "profit_total": 0,
    }
    portefeuilles = []
    # On créer une boucle pour créer les combinaisons de 1 à 20 actions
    for i in range(nb_action_min, nb_action_max + 1):
        # Va repeter la boucle pour chaque combinaison en commençant par 1 action puis 2 puis 3 etc...
        for comb in combinations(actions, i):
            # Pour chaque combinaison on vérifie que le portefeuille que la somme des prix des actions est inférieur à 500
            if verif_portefeuille(comb):
                nb_combinaisons_true += 1

                # Donne le nom du portefeuille
                portefeuille["name_portefeuille"] = "portefeuille" + str(nb_combinaisons_true)
                # Donne la liste des actions du portefeuille
                portefeuille["actions"] = comb
                # Donne le profit total du portefeuille
                portefeuille["profit_total"] = sum([action["profit"] for action in comb])
                # On ajoute le portefeuille à la liste des portefeuilles
                portefeuilles.append(portefeuille.copy())

            else :
                nb_combinaisons_false += 1
    # On classe les portefeuilles par profit total décroissant
    # Calcul du profit pour chaque action individuellement

    portefeuilles = sorted(portefeuilles, key=lambda k: k['profit_total'], reverse=True)
    # On sauvegarde les portefeuilles dans un fichier csv
    save_portefeuille_actions(portefeuilles, "portefeuilles.csv")
    print("Nombre de combinaisons justes : " + str(nb_combinaisons_true))
    print("Nombre de combinaisons fausses : " + str(nb_combinaisons_false))

def verif_portefeuille(portefeuille):
    # On vérifie que la somme des prix des actions est inférieur à 500
    if sum([action["price"] for action in portefeuille]) <= 500:
        # print la somme des prix des actions
        # print(sum([action["price"] for action in portefeuille]))
        return True
    else :
        # print la somme des prix des actions
        # print(sum([action["price"] for action in portefeuille]))
        return False
    
# On stockent les informations dans un fichier csv
def save_portefeuille_actions(portefeuille_actions, portefeuille_name):
    # On créer un dossier pour stocker les portefeuilles
    os.makedirs("portefeuilles", exist_ok=True)
    # On créer le chemin du fichier
    portefeuille_name = os.path.join("portefeuilles", portefeuille_name)
    # On créer le fichier csv
    with open(portefeuille_name, "w") as csvfile:
        # On créer un objet writer
        writer = csv.writer(csvfile)
        # On écrit les données dans le fichier csv
        writer.writerow(["name_portefeuille", "actions", "profit_total"])
        for portefeuille in portefeuille_actions:
            writer.writerow([portefeuille["name_portefeuille"], portefeuille["actions"], portefeuille["profit_total"]])

# Definir la notation big O 
# O(n^2) car on a une boucle imbriquée 


# Eexecute la fonctio
if __name__ == "__main__":
    # Definir la notation big O 
    
    # On calcul le profit de chaque action
    actions = calcul_profit(actions)
    # On créer les portefeuilles d'actions
    create_portefeuille_actions(actions)