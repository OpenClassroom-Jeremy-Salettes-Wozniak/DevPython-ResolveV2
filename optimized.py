import csv

def read_csv(file_path):
    data = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

def calcul_profit(actions):
    # On calcule le profit de chaque action
    for action in actions:
        # Modifier le prix en float
        action["price"] = float(action["price"])
        # On calcule le profit en multipliant le prix par le pourcentage de profit
        action["profit"] = float(action["price"]) * float(action["profit"]) / 100
    return actions

# def knapsack(budget, actions, n):
#     # Initialisation de la matrice
#     matrice = [[0 for x in range(budget + 1)] for x in range(n + 1)]
 
#     # On remplit la matrice
#     for i in range(n + 1):
#         for j in range(budget + 1):
#             if i == 0 or j == 0:
#                 matrice[i][j] = 0
#             elif actions[i-1][0] <= j:
#                 matrice[i][j] = max(actions[i-1][1] + matrice[i-1][j-actions[i-1][0]],  matrice[i-1][j])
#             else:
#                 matrice[i][j] = matrice[i-1][j]
 
#     return matrice[n][budget]

# Official

def knapsack(capacity: float, weights: list[float], values: list[float], counter: float) -> float:
    """
    Returns the maximum value that can be put in a knapsack of a capacity cap,
    whereby each weight w has a specific value val.

    >>> cap = 50
    >>> val = [60, 100, 120]
    >>> w = [10, 20, 30]
    >>> c = len(val)
    >>> knapsack(cap, w, val, c)
    220

    The result is 220 cause the values of 100 and 120 got the weight of 50
    which is the limit of the capacity.
    """

    # Base Case
    if counter == 0 or capacity == 0:
        return 0

    # If weight of the nth item is more than Knapsack of capacity,
    #   then this item cannot be included in the optimal solution,
    # else return the maximum of two cases:
    #   (1) nth item included
    #   (2) not included
    if weights[counter - 1] > capacity:
        return knapsack(capacity, weights, values, counter - 1)
    else:
        left_capacity = capacity - weights[counter - 1]
        new_value_included = values[counter - 1] + knapsack(
            left_capacity, weights, values, counter - 1
        )
        without_new_value = knapsack(capacity, weights, values, counter - 1)
        return max(new_value_included, without_new_value)

if __name__ == "__main__":
    budget = 500
    # data = [
    #     {
    #         "name": "action1",
    #         "price": 20,
    #         "profit": 5
    #     },
    #     {
    #         "name": "action2",
    #         "price": 30,
    #         "profit": 10
    #     },
    #     {
    #         "name": "action3",
    #         "price": 50,
    #         "profit": 15
    #     },
    #     {
    #         "name": "action4",
    #         "price": 70,
    #         "profit": 20
    #     },
    #     {
    #         "name": "action5",
    #         "price": 60,
    #         "profit": 17
    #     },
    #     {
    #         "name": "action6",
    #         "price": 80,
    #         "profit": 25
    #     },
    #     {
    #         "name": "action7",
    #         "price": 22,
    #         "profit": 7
    #     },
    #     {
    #         "name": "action8",
    #         "price": 26,
    #         "profit": 11
    #     },
    #     {
    #         "name": "action9",
    #         "price": 48,
    #         "profit": 13
    #     },
    #     {
    #         "name": "action10",
    #         "price": 34,
    #         "profit": 27
    #     },
    #     {
    #         "name": "action11",
    #         "price": 42,
    #         "profit": 17
    #     },
    #     {
    #         "name": "action12",
    #         "price": 110,
    #         "profit": 9
    #     },
    #     {
    #         "name": "action13",
    #         "price": 38,
    #         "profit": 23
    #     },
    #     {
    #         "name": "action14",
    #         "price": 14,
    #         "profit": 1
    #     },
    #     {
    #         "name": "action15",
    #         "price": 18,
    #         "profit": 3
    #     },
    #     {
    #         "name": "action16",
    #         "price": 8,
    #         "profit": 8
    #     },
    #     {
    #         "name": "action17",
    #         "price": 4,
    #         "profit": 12
    #     },
    #     {
    #         "name": "action18",
    #         "price": 10,
    #         "profit": 14
    #     },
    #     {
    #         "name": "action19",
    #         "price": 24,
    #         "profit": 21
    #     },
    #     {
    #         "name": "action20",
    #         "price": 114,
    #         "profit": 18
    #     },
    # ]

    data = read_csv("dataset1_PythonP7.csv")

    actions = calcul_profit(data) # Exemple : [ { "name": "action1", "price": 250, "profit": 0.5 }, ... 
    # actions = actions[1::]
    list_price = []
    list_profit = []
    i = 0
    for action in actions:
        if action["price"] == 0:
            i += 1
            continue
        list_price.append(action["price"]) # poids
        list_profit.append(action["profit"]) # valeur
    lenaction = len(actions) - i
    print(lenaction)
    print(len(list_profit))
    print(len(list_price))
    result = knapsack(budget, list_price, list_profit, lenaction)
    # print(result)