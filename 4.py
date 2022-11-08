"""
Exercice:
    Faire un MJ qui affiche un message lorsque input renvoie le bon caractere
    Le charactere doit être parametrable
"""

character = 'x'

# Pendant que input renvoye quelquechose different de character
# Si l'input et égal a character, la boucle sera finie
while input("Devine le caractère secret...> ") != character:
    # Afficher "Mauvaise réponse!"
    print("Mauvaise réponse!")

# Afficher "Bien joué!" une fois la boucle finie
print("Bien joué!")