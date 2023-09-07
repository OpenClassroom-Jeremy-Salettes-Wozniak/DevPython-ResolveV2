# Résolvez des problèmes en utilisant des algorithmes en Python

--- 

## Cours : Découvrez le fonctionnement des algorithmes

Un algorithmes est un ensemble de ligne de code qui execute une tache donnée.

### Pseudocode
Pour comprendre un algorithmes il faut le divisé en sous algorithmes et pour mieux le comprendre l'écrire en pseudo-code.

```code
<!-- VOICI DU PSEUDO-CODE -->
DEBUT
    REPETE TANT QUE LE C'EST PAS VRAIS
        DEPLACEMENT VERS LA DROITE
        DEPLACEMENT VERS LE HAUT
FIN
```

---

### Les variables et types de données

Les variables font références à un objet cela peut etre :

#### Type de données

- Chaine de caractère(string)
- Un nombre entier ou a virgule (int, float)
- Un booleen (vrais ou faux)
- Une liste (modifiable) (value0, value1, value2, ...)
- Dictionnaire (modifiable){ "key" : "value", ... }

#### Les variables non modifiable (constante et turple)

- Chaine de caractère(string)
- Un nombre entier ou a virgule (int, float)
- Un booleen (vrais ou faux)
- Une turple (une liste non modifiable)

#### Autre variables

Une variable ou constante peut contenir des function avec des valeurs définis ou encore des instances de classes(usine)

- Functions
- Instance de classes

```code
Variable
    déplacement ← 0
    score ← 0
Début
Fin     
```

Les fonctions font référence à un bloc d'instruction qui attende généralement une valeur en entrée et qui retour une autre valeur en sortie apres avoir executez les différentes actions demande à l'intérieur de la fonction.

```code
Fonction maj_déplacement_score(déplacement, score, point_de_déplacement)
Début
    déplacement ← déplacement + 1
    score ← score + point_de_déplacement
Fin
```

---

## Structures conditionnelles

Une condition c'est pour savoir si une valeur à atteint son objectif ou non et retour true ou false

```CODE
SI (CONDITIONS1 VRAIS){
    EXECUTE LE CODE
}
SINON SI (CONDITIONS2 VRAIS){
    EXECUTE LE CODE
}
SINON {
    EXECUTE LE CODE
}

CONDITION D'EGALITE : 
SI (VALUE == "success"){
    EXECUTE LE CODE SI EGALE
}
SI (VALUE === "success"){
    EXECUTE LE CODE SI EGALE (Prend en compte le type de donnée)
}
CONDITION DE INFERIEUR / INFERIEUR OU EGALE : 
SI (VALUE < 5) {
    EXECUTE LE CODE SI INFERIEUR
}
SI (VALUE <= 5) {
    EXECUTE LE CODE SI INFERIEUR OU EGALE 
}
SI (VALUE <== 5) {
    EXECUTE LE CODE SI STRICTEMENT INFERIEUR OU EGALE (Prend en compte le type de donnée)
}

CONDITION DE SUPERIEUR / SUPERIEUR OU EGALE : 
SI (VALUE > 5) {
    EXECUTE LE CODE SI SUPERIEUR
}
SI (VALUE >= 5) {
    EXECUTE LE CODE SI SUPERIEUR OU EGALE 
}
SI (VALUE <== 5) {
    EXECUTE LE CODE SI STRICTEMENT INFERIEUR OU EGALE (Prend en compte le type de donnée)
}

CONDITION DE DIFFERENCE
SI (VALUE != 5) {
    EXECUTE LE CODE SI DIFFERENCE
}
SI (VALUE !== 5) {
     EXECUTE LE CODE SI STRICTEMENT DIFFERENCE (Prend en compte le type de donnée)
}

CONDITION ET :
SI (VALUE1 == TRUE AND VALUE2 == FALSE){
    EXECUTE LE CODE SI LA VALUE1 ET VRAI ET QUE LA VALUE2 ET FAUSSE
}

CONDITION OU :
SI (VALUE1 == TRUE OR VALUE2 == TRUE){
    EXECUTE LE CODE SI LA VALUE1 ET VRAI OU BIEN QUE LA VALUE2 ET VRAI
}
```

## Les boucles

WHILE REPETE TANT QUE LA CONDITION N'EST PAS VRAI

```CODE
while(CONDITION == FALSE){
    EXECUTE LE CODE TANT QUE LA CONDITION N'EST PAS VRAI
}
```

FOR REPETE UN CERTAIN NOMBRE DE FOIS

```CODE
NUM = 10
for(i = 0; i < NUM - 1; i++){
    EXECUTE LE CODE JUSQU'A QUE i ATEIGNE 10
}
```

## ARBRE BINAIRE ET GRAPH

Les arbres binaires et les graph sont la maniere dont nous stockons chaque objet avec d'autre objet:

- Un arbre contient des liers vers deux autre objet on appelle cela un arbre binaire
- Un arbre contient plusieurs branches c'est un arbre aleatoire
- Il y a interconnecion avec plusieurs objet connecter avec d'autre objet graph

## ALGORITHM DE TRIE

On a besoin de trier les données constament certain algorithme existe déja en voici quelque un : 

- Trie par selection : Le tri par sélection est un algorithme de tri qui sélectionne à chaque itération le plus petit élément d'une liste non triée, et place cet élément au début de la liste non triée.
  
```code
```

- Trie à bulles : Permet de commparer deux elements d'une liste ensemble et les échanges si la l'une d'est valeur et plus elevez.
  
```code
```

- Tri par insertion : considère chaque élément du tableau, et l'insère à la bonne place parmi les éléments déjà triés.

```code
```

- Tri par tas : Le tri par tas débute par la construction d'un tas sur le tableau d'entrée. Comme l'élément maximum du tableau est stocké à la racine, on peut le placer dans sa position finale correcte en l'échangeant avec le dernier élément du tableau.

```code
```

- Tri par fusion : Le tri par fusion fonctionne sur le principe de diviser pour mieux régner. Le tri par fusion décompose à plusieurs reprises une liste en plusieurs sous-listes jusqu'à ce que chaque sous-liste se compose d'un seul élément, et fusionne ces sous-listes de manière à obtenir une liste triée.

```code
```

## COMPLEXITER ALGORITHM


## Introduction

- Investissement à court terme plus compétitifs. Concevoir un algorithme qui maximisera le profit réalisé par nos clients après deux ans d'investissement.
- Votre algorithme doit suggérer une liste des actions les plus rentables que nous devrions acheter pour maximiser le profit d'un client au bout de deux ans.
- Chaque action ne peut être achetée qu'une seule fois.
- Nous pouvons dépenser au maximum 500 euros par client.

| Action     | Coût par action (en euros) | Bénéfice (après 2 ans) |
|------------|---------------------------:|-----------------------:|
| Action-1   |                        20  |                    5% |
| Action-2   |                        30  |                   10% |
| Action-3   |                        50  |                   15% |
| Action-4   |                        70  |                   20% |
| Action-5   |                        60  |                   17% |
| Action-6   |                        80  |                   25% |
| Action-7   |                        22  |                    7% |
| Action-8   |                        26  |                   11% |
| Action-9   |                        48  |                   13% |
| Action-10  |                        34  |                   27% |
| Action-11  |                        42  |                   17% |
| Action-12  |                       110  |                    9% |
| Action-13  |                        38  |                   23% |
| Action-14  |                        14  |                    1% |
| Action-15  |                        18  |                    3% |
| Action-16  |                         8  |                    8% |
| Action-17  |                         4  |                   12% |
| Action-18  |                        10  |                   14% |
| Action-19  |                        24  |                   21% |
| Action-20  |                       114  |                   18% |

```code

# # On créer une liste avec les actions et la rentabilité
# liste_actions_rentabilite = []
# for action in liste_actions:
#     # Calcul de la rentabilité
#     rentabilite = liste_actions[action]["prix"] * liste_actions[action]["pourcentage"] / 100
#     # On ajoute la rentabilité à la liste
#     liste_actions_rentabilite.append([action, rentabilite])

# # On trie la liste par ordre de rentabilité
# # Explique key=lambda x: x[1] et reverse=True
# # Key permet de dire sur quel élément on veut trier
# # algorie de tri: https://www.geeksforgeeks.org/python-list-sort/

# liste_actions_rentabilite.sort(key=lambda x: x[1], reverse=True)

# print(liste_actions_rentabilite)

```
