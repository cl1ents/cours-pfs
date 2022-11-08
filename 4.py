"""
Exercice:
    Faire un MJ qui affiche un message lorsque input renvoie le bon caractere
    Le charactere doit être parametrable
"""

"""
import random

# Definir l'alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"
# Puis choisir une lettre aléatoirement
letter = random.choice(alphabet)
"""

# Definir la lettre secrette
letter = "x"

tries = 0

# Pendant que input renvoye quelquechose different de letter
# Si l'input et égal a letter, la boucle sera finie
while input("Devine la lettre secrette...> ").lower() != letter.lower():
    # Incrémenter le nombre d'essais...
    tries = tries + 1
    # Afficher "Mauvaise réponse! <tries>"
    print(f"Mauvaise réponse! Tu es a {tries} essais.")

# Afficher "Bien joué!" une fois la boucle finie
print("Bien joué!")

# ah oui la vrm les bananes grimper aux arbres pour manger OUHAZOUHAHAOUHAHA