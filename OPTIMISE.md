### Importer la bibliothèque CSV
import csv

### Fonction pour lire un fichier CSV et renvoyer les données sous forme de liste de dictionnaires
Fonction lire_csv(chemin_fichier):
    Données = Liste Vide
    Ouvrir le fichier au chemin_fichier en mode lecture (encodé en UTF-8)
    Pour chaque ligne dans le fichier:
        Ajouter la ligne sous forme de dictionnaire à la liste de données
    Retourner les données

### Fonction pour calculer le profit pour chaque action
Fonction calculer_profit(actions):
    Actions_avec_profit = Liste Vide
    Pour chaque action dans les actions:
        Prix = Convertir en nombre à virgule flottante (action["price"])
        Profit = (Prix * Convertir en nombre à virgule flottante (action["profit"])) / 100
        Si Prix > 0 et Profit > 0:
            Ajouter un dictionnaire avec le nom, le prix et le profit calculé à Actions_avec_profit
    Retourner Actions_avec_profit

### Fonction pour récupérer les actions sélectionnées en utilisant la programmation dynamique
Fonction récupérer_actions(dp, poids, nom):
    Actions = Liste Vide
    n = Longueur de dp - 1
    w = Longueur de dp[0] - 1
    Tant que n > 0 et w > 0:
        Si dp[n][w] est différent de dp[n - 1][w]:
            Ajouter le nom[n - 1] à la liste d'actions
            Réduire w de poids[n - 1]
        Réduire n de 1
    Retourner Actions

### Fonction pour résoudre le problème du sac à dos 0/1
Fonction sac_a_dos_01(W, prix, profit, n, name):
    Créer un tableau dynamique dp de dimensions (n + 1) x (W + 1) initialisé à 0
    Pour i allant de 0 à n:
        Pour w allant de 0 à W:
            Si i est égal à 0 ou w est égal à 0:
                Affecter 0 à dp[i][w]
            Sinon si prix[i - 1] est inférieur ou égal à w:
                Affecter le maximum entre (profit[i - 1] + dp[i - 1][w - prix[i - 1]]) et dp[i - 1][w] à dp[i][w]
            Sinon:
                Affecter dp[i - 1][w] à dp[i][w]
    Retourner dp[n][W] et l'appel à la fonction récupérer_actions avec dp, prix et name

### Point d'entrée du programme
Si __name__ est égal à "__main__":
    Données = Liste d'actions avec noms, prix et profits
    Budget = 500
    Données = Appeler la fonction lire_csv avec le chemin du fichier CSV
    Actions = Appeler la fonction calculer_profit avec les données
    Initialiser des listes pour stocker les noms, prix et profits des actions
    Pour chaque action dans les actions:
        Ajouter le nom de l'action à la liste des noms
        Ajouter le prix de l'action (converti en entier) à la liste des prix
        Ajouter le profit de l'action (converti en entier) à la liste des profits
    Calculer la longueur totale des actions
    Résultat = Appeler la fonction sac_a_dos_01 avec le budget, la liste des prix, la liste des profits, la longueur des actions et la liste des noms
    Afficher le résultat

### La complexité de cet algorithme est O(n * W), où "n" est le nombre d'articles et "W" est la capacité maximale.
