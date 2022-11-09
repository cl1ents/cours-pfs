# DEBUT

# On admet une fonction `createGrid` qui renvoye une liste de longueur X, rempli de listes de longueurs Y qui eux sont remplis de nombres aléatoires (ou prédefinis (sûrement prédefinis, d'ailleurs))
from random import randint, seed
## SET THE SEED TO GET A "FIXED" GRID!
seed(1)

"""
Creates grid of X by Y
"""
def createGrid(X, Y):
    result = []
    for _ in range(X):
        result.append([randint(0,9) for _ in range(Y)])
    return result

print(createGrid(10,10))

# FIN