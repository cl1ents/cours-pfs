# DEBUT

# On admet une fonction `random` qui renvoie un chiffre entre 0 et 2
# On admet une fonction `clear` qui effact tout le texte affiché
# On admet une fonction `input` avec un argument `Text`:
    # Afficher la valeur de `Text`
    # Attendre que l'utilisateur entre une chaine de caractère, puis la renvoyer

# Definir une liste `nomActions` avec:
    # "Pierre" en tant qu'élément 0,
    # "Feuille" en tant qu'élément 1,
    # et "Ciseaux" en tant qu'élément 2

# On admet une fonction `checkInt` qui permet de verifier si une chaine de caractere peut être un nombre entier

# Definir un boolean True `playing`

# Pendant que playing est True:
    # Definir `actionBot` en tant que le retour de la fonction `random`
    # Definir `actionPlayer` en tant que chaine de caractere vide
    # Tant que `actionPlayer` n'est pas un nombre entier ou que ce nombre n'est pas compris entre 0 et 2:
        # Afficher "0 = Pierre, 1 = Feuille, 2 = Ciseaux"
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
        # Afficher "DRAW!"
    # Sinon si: 
     # `actionBot` est égal a Pierre et `actionPlayer` est égal a Ciseaux
     # ou `actionBot` est égal a Ciseaux et `actionPlayer` est égal a Feuille
        # Afficher "BOT WINS!"
    # Sinon si:
     # `actionPlayer` est égal a Pierre et `actionBot` est égal a Ciseaux
     # ou `actionPlayer` est égal a Ciseaux et `actionBot` est égal a Feuille
        # Afficher "YOU WIN!"
        # Mettre `playing` a False

# FIN