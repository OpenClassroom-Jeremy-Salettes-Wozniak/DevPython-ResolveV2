import csv

def read_csv(file_path):
    data = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

def calcul_profit(actions):
    actions_avec_profit = []
    for action in actions:
        price = float(action["price"])
        profit = float(action["price"]) * float(action["profit"]) / 100
        # Si le prix et le profit sont supérieurs à 0, alors on les ajoute
        if price > 0 and profit > 0:
            actions_avec_profit.append({"name": action["name"], "price": price, "profit": profit})
    return actions_avec_profit

def knapSack(W, wt, val, n):
    # Créez un tableau pour stocker les résultats intermédiaires
    dp = [[0 for x in range(W + 1)] for x in range(n + 1)]
    # Remplissez le tableau dp en utilisant la programmation dynamique
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][W]

if __name__ == "__main__":

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

    budget = 500
    # data = read_csv("dataset2_PythonP7.csv")
    actions = calcul_profit(data)
    print(actions)

    list_price = []
    list_profit = []

    for action in actions:
        list_price.append(int(action["price"]))  # Convertir le prix en entier
        list_profit.append(int(action["profit"]))  # Convertir le profit en entier

    lenaction = len(actions)

    result = knapSack(budget, list_price, list_profit, lenaction)

    print(result)
