# DEBUT

from time import sleep

# On admet une fonction `random` qui renvoie un chiffre entre 0 et 2
from random import randint
def random():
    return randint(0, 2)
# On admet une fonction `clear` qui effact tout le texte affiché
from os import system, name as osname
def clear():
    system('cls' if osname=='nt' else 'clear')

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

# Definir un dictionnaire `languages` avec:
languages = {
    # Une liste d'index "fr" avec:
        # "Pierre" en tant qu'élément 0,
        # "Feuille" en tant qu'élément 1,
        # et "Ciseaux" en tant qu'élément 2
    'fr': ["Pierre", "Feuille", "Ciseaux"],
    # Une liste d'index "en" avec:
        # "Rock" en tant qu'élément 0,
        # "Paper" en tant qu'élément 1,
        # et "Scissors" en tant qu'élément 2
    'fenr': ["Rock", "Paper", "Scissors"],
    # Une liste d'index "zh" avec:
        # "Chi" en tant qu'élément 0,
        # "Fu" en tant qu'élément 1,
        # et "Mi" en tant qu'élément 2
    'zh': ["Chi", "Fu", "Mi"],
    # Une liste d'index "jp" avec:
        # "Jan" en tant qu'élément 0,
        # "Ken" en tant qu'élément 1,
        # et "Pon" en tant qu'élément 2
    'jp': ["Jan", "Ken", "Pon"],
}


# Definir une fonction `round` qui prend pour argument une chaine de caractere `language`:
def round(language):
    # Definir une variable `nomActions` qui prend pour valeur l'élement d'index `language` dans `languages`
    nomActions = languages[language]
    # Pendant que True:
    while True:
        # Definir `actionBot` en tant que le retour de la fonction `random`
        actionBot = random()
        # Definir `actionPlayer` en tant que chaine de caractere vide
        actionPlayer = ''
        # Tant que `actionPlayer` n'est pas un nombre nombre entier ou que ce nombre n'est pas compris entre 0 et 2:
        while (not checkInt(actionPlayer)) or int(actionPlayer) < 0 or int(actionPlayer) > 2:
            # Afficher "0 = Pierre, 1 = Feuille, 2 = Ciseaux"
            print("\n0 = Pierre, 1 = Feuille, 2 = Ciseaux")
            # Redefinir `actionPlayer` en tant que le retour de la fonction `input` avec argument "> "
            actionPlayer = input("> ")
            # Appeler la fonction `clear`
            clear()
        
        intActionPlayer = int(actionPlayer)

        # Pour `Output` prennant toutes les valeurs dans `nomActions` dans l'ordre:
        for Output in nomActions:
            # Afficher `Output`
            print(Output)
            # Attendre 0.3 secondes
            sleep(.3)

        # Definir `Output` en tant que la concatenation de ces chaines de caractères:
        # "BOT: ", l'élement `nomActions` d'index `actionBot`, ", PLAYER: ", et enfin l'élement `nomActions` d'index `actionPlayer`
        # Afficher `Output`
        print("BOT: "+nomActions[actionBot]+", Player: "+nomActions[intActionPlayer])

        ### EN RETENANT QUE Pierre EST 0, Feuille EST 1 ET Ciseaux EST 2
        # Si `actionBot` est égal a `actionPlayer` alors:
        if actionBot == intActionPlayer:
            # Afficher "DRAW! RETRY."
            print("DRAW! RETRY.")
        # Sinon si: 
        # `actionBot` est égal a Pierre et `actionPlayer` est égal a Ciseaux
        # ou `actionBot` est égal a Ciseaux et `actionPlayer` est égal a Feuille
        elif (actionBot == 0 and intActionPlayer == 2) or (actionBot == 2 and intActionPlayer == 1):
            # Afficher "BOT WINS!"
            print("BOT WINS!")
            # Renvoyer False
            return False
        # Sinon si:
        # `actionPlayer` est égal a Pierre et `actionBot` est égal a Ciseaux
        # ou `actionPlayer` est égal a Ciseaux et `actionBot` est égal a Feuille
        elif (intActionPlayer == 0 and actionBot == 2) or (intActionPlayer == 2 and actionBot == 1):
            # Afficher "YOU WIN!"
            print("YOU WIN!")
            # Renvoyer True
            return True

# Definir une fonction `match` qui prend pour arguments une chaine de caractere `language` et un nombre entier `roundCount`
def match(language, roundCount):
    # Definir un nombre `botScore` qui prend pour valeur 0
    botScore = 0
    # Definir une nombre `playerScore` qui prend pour valeur 0
    playerScore = 0

    # Pour i prenant toutes les valeurs entre 0 et `roundCount`-1:
    for i in range(roundCount):
        # Afficher la concatenation entre "--- ROUND NUMBER ", i sous forme de chaine de caractere, et " ---"
        print("--- ROUND NUMBER "+str(i)+" ---")
        # Definir `Output` en tant que la concatenation de ces chaines de caractères:
        # "BOT: ", `botScore` sous forme d'une chaine de caractere, ",\nPLAYER: ", `playerScore` sous forme d'une chaine de caractere
        # Afficher `Output`
        print("BOT: " + str(botScore) + ",\nPLAYER: " + str(playerScore))

        # Definir un boolean `winner` qui prend pour valeur le retour de `round` avec argument `language`
        winner = round(language)

        # Si `winner` est égal a True,
        if winner:
            # Alors incrementer `playerScore` de 1
            playerScore += 1
        # Sinon,
        else:
            # Incrementer `botScore` de 1
            botScore += 1

    # Definir `Output` en tant que la concatenation de ces chaines de caractères:
    # "BOT: ", `botScore` sous forme d'une chaine de caractere, ",\nPLAYER: ", `playerScore` sous forme d'une chaine de caractere
    # Afficher `Output`
    print("BOT: " + str(botScore) + ",\nPLAYER: " + str(playerScore))

    # Si `botScore` est plus grand que `playerScore`,
    if botScore > playerScore:
        # Alors afficher "BOT WINS THE MATCH!"
        print("BOT WINS THE MATCH!")
        # Renvoyer False
        return False
    # Sinon,
    else:
        # Afficher "YOU WIN THE MATCH!"
        print("YOU WIN THE MATCH!")
        # Renvoyer True
        return True

# Definir une chaine de caractere vide `languageChosen`
languageChosen = ''
# Pendant que l'élément d'index `languageChosen` dans le dictionnaire `languages` n'éxiste pas:
while not languages.get(languageChosen):
    # Afficher "CHOOSE A LANGUAGE:"
    print("CHOOSE A LANGUAGE:")
    # Afficher "fr = Français, en = English, zh = Zhōngguó rén, jp = Nihongo"
    print("fr = Français, en = English, zh = Zhōngguó rén, jp = Nihongo")
    # Redefinir `languageChosen` en tant que le retour de la fonction `input` avec argument "> "
    languageChosen = input("> ")
    # Appeler la fonction `clear`
    clear()

# Definir `countChosen` en tant que chaine de caractere vide
countChosen = ''
# Tant que `countChosen` n'est pas un nombre entier:
while not checkInt(countChosen):
    # Afficher "HOW MANY ROUNDS?"
    print("HOW MANY ROUNDS?")
    # Redefinir `countChosen` en tant que le retour de la fonction `input` avec argument "> "
    countChosen = input("> ")
    # Appeler la fonction `clear`
    clear()

countChosenInt = int(countChosen)

# Afficher "LANGUAGE CHOSEN:"
print("LANGUAGE CHOSEN:")
# Afficher `languageChosen`
print(languageChosen)
# Afficher "ROUND COUNT:"
print("ROUND CHOSEN:")
# Afficher `countChosen`
print(countChosenInt)

# Appeler la fonction `match` avec `languageChosen` et `countChosen` comme arguments
match(languageChosen, countChosenInt)

# FIN