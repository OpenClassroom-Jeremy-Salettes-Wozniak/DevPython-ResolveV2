import csv

def read_csv(file_path):
    """
    Cette fonction lit un fichier CSV et renvoie les données sous forme de liste de dictionnaires.
    Chaque dictionnaire représente une ligne du fichier CSV.
    """
    data = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

def calcul_profit(actions):
    """
    Cette fonction calcule le profit pour chaque action en fonction du prix et du pourcentage de profit spécifiés
    dans chaque action, puis renvoie une liste d'actions avec leur profit calculé.

    :param actions: Une liste d'actions, chaque action étant un dictionnaire avec des clés "name" (nom de l'action),
    "price" (prix de l'action), et "profit" (pourcentage de profit attendu).

    :return: Une liste d'actions avec leur profit calculé, sous forme de dictionnaires contenant les clés "name" (nom de l'action),
    "price" (prix de l'action), et "profit" (profit calculé).
    """
    actions_avec_profit = []
    for action in actions:
        price = float(action["price"])
        profit = float(action["price"]) * float(action["profit"]) / 100
        # Si le prix et le profit sont supérieurs à 0, alors on les ajoute à la liste des actions avec profit.
        if price > 0 and profit > 0:
            actions_avec_profit.append({"name": action["name"], "price": price, "profit": profit})
    return actions_avec_profit

def get_actions(dp, poids, nom):
    """
    Cette fonction récupère les actions sélectionnées en fonction des résultats intermédiaires de la programmation dynamique.

    :param dp: Le tableau de programmation dynamique contenant les résultats intermédiaires du problème du sac à dos.
    :param poids: La liste des poids des articles.
    :param nom: La liste des noms correspondants aux articles.

    :return: Une liste d'actions sélectionnées en fonction des résultats intermédiaires du sac à dos 0/1.
    """
    actions = []
    n = len(dp) - 1
    w = len(dp[0]) - 1
    while n > 0 and w > 0:
        # Si la valeur diffère de celle au-dessus (c'est-à-dire l'article a été inclus), ajoutez-le à la liste d'actions.
        if dp[n][w] != dp[n - 1][w]:
            actions.append(nom[n - 1])
            w -= poids[n - 1]
        n -= 1
    return actions

def knapSack(W, prix, profit, n, name):
    """
    Résout le problème du sac à dos 0/1 dans le but de maximiser la valeur totale des articles sélectionnés,
    tout en garantissant que la capacité maximale du sac à dos (représentée par le budget disponible) ne soit pas dépassée.

    :param W: La capacité maximale du sac à dos (budget disponible).
    :param prix: La liste des prix des articles.
    :param profit: La liste des profits correspondants des articles.
    :param n: Le nombre total d'articles disponibles.
    :param name: La liste des noms des articles.

    :return: Un tuple contenant la valeur maximale atteinte du sac à dos et la liste des articles sélectionnés.
    """
    # Créez un tableau dynamique pour stocker les résultats intermédiaires (programmation dynamique)
    dp = [[0 for x in range(W + 1)] for x in range(n + 1)]
    
    # Remplissez le tableau dp en utilisant la programmation dynamique
    for i in range(n + 1):
        for w in range(W + 1):
            # Si aucun article n'est disponible ou si la capacité est nulle, la valeur est zéro.
            if i == 0 or w == 0:
                dp[i][w] = 0
            # Si le poids de l'article est inférieur ou égal à la capacité actuelle, déterminez la valeur maximale
            # entre le profit de l'article actuel ajouté à la meilleure valeur précédente et la valeur précédente sans cet article.
            elif prix[i - 1] <= w:
                dp[i][w] = max(profit[i - 1] + dp[i - 1][w - prix[i - 1]], dp[i - 1][w])
            # Sinon, la valeur est la même que la précédente sans cet article.
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Retourne la valeur maximale atteinte du sac à dos et la liste des articles sélectionnés
    return dp[n][W], get_actions(dp, prix, name)


if __name__ == "__main__":

    # données d'actions avec leurs noms, prix et profits
    data = [
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
    # Budget disponible pour l'investissement
    budget = 500

    # Lecture des données depuis un fichier CSV (peut être utilisé à la place de la liste "data")
    # data = read_csv("dataset1_PythonP7.csv")
    data = read_csv("dataset2_PythonP7.csv")

    # Calcul du profit pour chaque action
    actions = calcul_profit(data)

    # Initialisation de listes pour stocker les noms, prix et profits des actions
    list_name = []
    list_price = []
    list_profit = []

    # Extraction des informations des actions
    for action in actions:
        list_name.append(action["name"])
        list_price.append(int(action["price"]))  # Convertir le prix en entier
        list_profit.append(int(action["profit"]))  # Convertir le profit en entier

    # Nombre total d'actions disponibles
    lenaction = len(actions)

    # Résolution du problème du sac à dos 0/1 pour maximiser la valeur
    # en utilisant le budget comme capacité maximale
    result = knapSack(budget, list_price, list_profit, lenaction, list_name)

    # Affichage du portefeuille d'actions optimal
    print(result)