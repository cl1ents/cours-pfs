# DEBUT

# On admet une fonction `random` qui renvoie un chiffre entre 0 et 2
# On admet une fonction `clear` qui effact tout le texte affiché

# On admet une fonction `input` avec un argument `Text`:
    # Afficher la valeur de `Text`
    # Attendre que l'utilisateur entre une chaine de caractère, puis la renvoyer

# On admet une fonction `checkInt` qui permet de verifier si une chaine de caractere peut être un nombre entier

# Definir un dictionnaire `languages` avec:
    # Une liste d'index "fr" avec:
        # "Pierre" en tant qu'élément 0,
        # "Feuille" en tant qu'élément 1,
        # et "Ciseaux" en tant qu'élément 2
    # Une liste d'index "en" avec:
        # "Rock" en tant qu'élément 0,
        # "Paper" en tant qu'élément 1,
        # et "Scissors" en tant qu'élément 2
    # Une liste d'index "zh" avec:
        # "Chi" en tant qu'élément 0,
        # "Fu" en tant qu'élément 1,
        # et "Mi" en tant qu'élément 2
    # Une liste d'index "jp" avec:
        # "Jan" en tant qu'élément 0,
        # "Ken" en tant qu'élément 1,
        # et "Pon" en tant qu'élément 2

# Definir une fonction `round` qui prend pour argument une chaine de caractere `language`:
    # Definir une liste `nomActions` qui prend pour valeur l'élement d'index `language` dans `languages`

    # Pendant que True:
        # Definir `actionBot` en tant que le retour de la fonction `random`
        # Definir `actionPlayer` en tant que chaine de caractere vide
        # Tant que `actionPlayer` n'est pas un nombre entier ou que ce nombre n'est pas compris entre 0 et 2:
            # Definir `Output` en tant que la concatenation de ces chaines de caractères:
                # "0 = ", l'élement dans `nomActions` d'index 0, ", 1 = ",  l'élement dans `nomActions` d'index 1, ", 2 = ", et enfin l'élement `nomActions` d'index 2
            # Afficher `Output`
            # Redefinir `actionPlayer` en tant que le retour de la fonction `input` avec argument "> "
            # Appeler la fonction `clear`

        # Pour `Output` prennant toutes les valeurs dans `nomActions` dans l'ordre:
            # Afficher `Output`
            # Attendre 0.3 secondes

        # Definir `Output` en tant que la concatenation de ces chaines de caractères:
            # "BOT: ", l'élement dans `nomActions` d'index `actionBot`, ", PLAYER: ", et enfin l'élement dans `nomActions` d'index `actionPlayer`
        # Afficher `Output`

        ### EN RETENANT QUE Pierre EST 0, Feuille EST 1 ET Ciseaux EST 2
        # Si `actionBot` est égal a `actionPlayer` alors:
            # Afficher "DRAW! RETRY."
        # Sinon si: 
        # `actionBot` est égal a Pierre et `actionPlayer` est égal a Ciseaux
        # ou `actionBot` est égal a Ciseaux et `actionPlayer` est égal a Feuille
            # Afficher "BOT WINS!"
            # Renvoyer False
        # Sinon si:
        # `actionPlayer` est égal a Pierre et `actionBot` est égal a Ciseaux
        # ou `actionPlayer` est égal a Ciseaux et `actionBot` est égal a Feuille
            # Afficher "YOU WIN!"
            # Renvoyer True

# Definir une fonction `match` qui prend pour arguments une chaine de caractere `language` et un nombre entier `roundCount`
    # Definir un nombre `botScore` qui prend pour valeur 0
    # Definir une nombre `playerScore` qui prend pour valeur 0

    # Pour i prenant toutes les valeurs entre 0 et `roundCount`-1:
        # Afficher la concatenation entre "--- ROUND NUMBER ", i sous forme de chaine de caractere, et " ---"
        # Definir `Output` en tant que la concatenation de ces chaines de caractères:
        # "BOT: ", `botScore` sous forme d'une chaine de caractere, ",\nPLAYER: ", `playerScore` sous forme d'une chaine de caractere
        # Afficher `Output`

        # Definir un boolean `winner` qui prend pour valeur le retour de `round` avec argument `language`

        # Si `winner` est égal a True,
            # Alors incrementer `playerScore` de 1
        # Sinon,
            # Incrementer `botScore` de 1

    # Definir `Output` en tant que la concatenation de ces chaines de caractères:
    # "BOT: ", `botScore` sous forme d'une chaine de caractere, ",\nPLAYER: ", `playerScore` sous forme d'une chaine de caractere
    # Afficher `Output`

    # Si `botScore` est plus grand que `playerScore`,
        # Alors afficher "BOT WINS THE MATCH!"
        # Renvoyer False
    # Sinon,
        # Afficher "YOU WIN THE MATCH!"
        # Renvoyer True

# Definir une chaine de caractere vide `languageChosen`
# Pendant que l'élément d'index `languageChosen` dans le dictionnaire `languages` n'éxiste pas:
    # Afficher "CHOOSE A LANGUAGE:"
    # Afficher "fr = Français, en = English, zh = Zhōngguó rén, jp = Nihongo"
    # Redefinir `languageChosen` en tant que le retour de la fonction `input` avec argument "> "
    # Appeler la fonction `clear`

# Definir `countChosen` en tant que chaine de caractere vide
# Tant que `countChosen` n'est pas un nombre entier:
    # Afficher "HOW MANY ROUNDS?"
    # Redefinir `countChosen` en tant que le retour de la fonction `input` avec argument "> "
    # Appeler la fonction `clear`

# Afficher "LANGUAGE CHOSEN:"
# Afficher `languageChosen`
# Afficher "ROUND COUNT:"
# Afficher `countChosen`

# Appeler la fonction `match` avec `languageChosen` et `countChosen` comme arguments


# FIN