# DEBUT

# On admet une fonction `random` qui renvoie un chiffre entre 0 et 2
from random import randint
def random():
    return randint(0, 2)

# On admet une fonction `input` avec un argument `Text`:
    # Afficher la valeur de `Text`
    # Attendre que l'utilisateur entre une chaine de caractère, puis la renvoyer

# On admet une fonction `checkInt` qui permet de verifier si une chaine de caractere peut être un nombre entier
def checkInt(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

# Definir une liste `nomActions` avec:
    # "Pierre" en tant qu'élément 0,
    # "Feuille" en tant qu'élément 1,
    # et "Ciseaux" en tant qu'élément 2
nomActions = ["Pierre", "Feuille", "Ciseaux"]

# Definir un boolean True `playing`
playing = True

# Pendant que playing est True:
while playing:
    # Definir `actionBot` en tant que le retour de la fonction `random`
    actionBot = random()
    # Afficher "0 = Pierre, 1 = Feuille, 2 = Ciseaux"
    print("\n0 = Pierre, 1 = Feuille, 2 = Ciseaux")
    # Definir `actionPlayer` en tant que le retour de la fonction `input` avec argument "> "
    actionPlayer = input("> ")
    # Tant que `actionPlayer` n'est pas un nombre nombre entier ou que ce nombre n'est pas compris entre 0 et 2:
    while (not checkInt(actionPlayer)) or int(actionPlayer) < 0 or int(actionPlayer) > 2:
        # Redefinir `actionPlayer` en tant que le retour de la fonction `input` avec argument "> "
        actionPlayer = input("> ")
    
    intActionPlayer = int(actionPlayer)

    # Definir `Output` en tant que la concatenation de ces chaines de caractères:
     # "BOT: ", l'élement `nomActions` d'index `actionBot`, ", PLAYER: ", et enfin l'élement `nomActions` d'index `actionPlayer`
    # Afficher `Output`
    print("BOT: "+nomActions[actionBot]+", Player: "+nomActions[intActionPlayer])

    ### EN RETENANT QUE Pierre EST 0, Feuille EST 1 ET Ciseaux EST 2
    # Si `actionBot` est égal a `actionPlayer` alors:
    if actionBot == intActionPlayer:
        # Afficher "DRAW!"
        print("DRAW!")
    # Sinon si: 
     # `actionBot` est égal a Pierre et `actionPlayer` est égal a Ciseaux
     # ou `actionBot` est égal a Ciseaux et `actionPlayer` est égal a Feuille
    elif (actionBot == 0 and intActionPlayer == 2) or (actionBot == 2 and intActionPlayer == 1):
        # Afficher "BOT WINS!"
        print("BOT WINS!")
    # Sinon si:
     # `actionPlayer` est égal a Pierre et `actionBot` est égal a Ciseaux
     # ou `actionPlayer` est égal a Ciseaux et `actionBot` est égal a Feuille
    elif (intActionPlayer == 0 and actionBot == 2) or (intActionPlayer == 2 and actionBot == 1):
        # Afficher "YOU WIN!"
        print("YOU WIN!")
        # Mettre `playing` a False
        playing = False

# FIN