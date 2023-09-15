import matplotlib.pyplot as plt
import numpy as np

# Créer un échantillon de valeurs de n (nombre d'actions)
n_values = np.arange(1, 21)  # De 1 à 20 actions

# Calculer la complexité O(n * 2^n) pour chaque valeur de n
complexity_values_1 = n_values * 2**n_values

# Calculer la complexité O(n^2) pour chaque valeur de n
complexity_values_2 = n_values**2

# Créer les graphiques
plt.figure(figsize=(12, 6))

# Premier graphique pour O(n * 2^n)
plt.subplot(1, 2, 1)
plt.plot(n_values, complexity_values_1, marker='o', linestyle='-', color='b')
plt.xlabel('Nombre d\'actions (n)')
plt.ylabel('Complexité (O(n * 2^n))')
plt.title('Complexité O(n * 2^n) en fonction du nombre d\'actions')
plt.grid(True)

# Deuxième graphique pour O(n^2)
plt.subplot(1, 2, 2)
plt.plot(n_values, complexity_values_2, marker='o', linestyle='-', color='r')
plt.xlabel('Nombre d\'actions (n)')
plt.ylabel('Complexité (O(n^2))')
plt.title('Complexité O(n^2) en fonction du nombre d\'actions')
plt.grid(True)

plt.tight_layout()
plt.show()
