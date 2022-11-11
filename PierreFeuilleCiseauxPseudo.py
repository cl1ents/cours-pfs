# DEBUT

# On admet une fonction `random` qui renvoie un chiffre entre 0 et 2
# On admet une fonction `clear` qui effact tout le texte affiché

# On admet une fonction `input` avec un argument `Text`:
    # Afficher la valeur de `Text`
    # Attendre que l'utilisateur entre une chaine de caractère, puis la renvoyer

# On admet une fonction `checkInt` qui permet de verifier si une chaine de caractere peut être un nombre entier

# Definir un dictionnaire `languages` avec:
    # Une liste `fr` avec:
        # "Pierre" en tant qu'élément 0,
        # "Feuille" en tant qu'élément 1,
        # et "Ciseaux" en tant qu'élément 2
    # Une liste `en` avec:
        # "Rock" en tant qu'élément 0,
        # "Paper" en tant qu'élément 1,
        # et "Scissors" en tant qu'élément 2
    # Une liste `zh` avec:
        # "Chi" en tant qu'élément 0,
        # "Fu" en tant qu'élément 1,
        # et "Mi" en tant qu'élément 2
    # Une liste `jp` avec:
        # "Jan" en tant qu'élément 0,
        # "Ken" en tant qu'élément 1,
        # et "Pon" en tant qu'élément 2

# Definir une fonction `round` qui prend pour argument une chaine de caractere `language`:
    # Definir une variable `nomActions` qui prend pour valeur l'élement d'index `language` dans `languages`
    # Definir un boolean True `playing`

    # Pendant que playing est True:
        # Definir `actionBot` en tant que le retour de la fonction `random`
        # Afficher "0 = Pierre, 1 = Feuille, 2 = Ciseaux"
        # Definir `actionPlayer` en tant que le retour de la fonction `input` avec argument "> "
        # Tant que `actionPlayer` n'est pas un nombre entier ou que ce nombre n'est pas compris entre 0 et 2:
            # Appeler la fonction `clear`
            # Afficher "0 = Pierre, 1 = Feuille, 2 = Ciseaux"
            # Redefinir `actionPlayer` en tant que le retour de la fonction `input` avec argument "> "

        # Pour `Output` prennant toutes les valeurs dans `nomActions` dans l'ordre:
            # Afficher `Output`
            # Attendre 0.3 secondes

        # Definir `Output` en tant que la concatenation de ces chaines de caractères:
        # "BOT: ", l'élement `nomActions` d'index `actionBot`, ", PLAYER: ", et enfin l'élement `nomActions` d'index `actionPlayer`
        # Afficher `Output`

        ### EN RETENANT QUE Pierre EST 0, Feuille EST 1 ET Ciseaux EST 2
        # Si `actionBot` est égal a `actionPlayer` alors:
            # Afficher "DRAW!"
            # Renvoyer -1
        # Sinon si: 
        # `actionBot` est égal a Pierre et `actionPlayer` est égal a Ciseaux
        # ou `actionBot` est égal a Ciseaux et `actionPlayer` est égal a Feuille
            # Afficher "BOT WINS!"
            # Renvoyer 0
        # Sinon si:
        # `actionPlayer` est égal a Pierre et `actionBot` est égal a Ciseaux
        # ou `actionPlayer` est égal a Ciseaux et `actionBot` est égal a Feuille
            # Afficher "YOU WIN!"
            # Mettre `playing` a False
            # Renvoyer 1

# Definir une fonction `match` qui prend pour arguments une chaine de caractere `language` et un nombre entier `winGoal`
    # Appeler la fonction `round` avec comme argument "fr" #FOR REEEEEEEAL

# FIN

"""
TODO:
- Finsh match system
- Add menu before starting for settings
- MAYBE clickable console stuff
- Add Player VS Player system
- Change the player input system into a function (so I can use it twice without redundancy)
"""