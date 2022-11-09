liste = [1,85,515,15,687,89,4,1,56,63,23,1,54,0,45,12,634,10]

"""
# Pour recuperer 15 je prend dans la liste l'index 4-1
print(liste[3]) # Renvoye 15
len(liste) # Renvoye la longueur de la liste

firstName = "Ta"
lastName = "Mere"
num = 564

fullName = firstName + " " + lastName + " #" + str(num)
"""

"""
Exercice 1:
    Faire une fonction qui concatene 2 chaines de caractere, les séparants par une virgule
"""
def concat(chaineA, chaineB):
    # Assurer qu'ils sont des str
    # (Changer le type de a et de b en string)
    stringifiedChaineA = str(chaineA)
    stringifiedChaineB = str(chaineB)
    # Retourner 
    return stringifiedChaineA + ", " + stringifiedChaineB

"""
Exercice 2:
    Faire une fonction qui itere sur tous les index d'un tableau renvoyant une chaine de
    caractere avec l'ensemble des occuration d'un chiffre
    e.g.: Pour tableau [0,1,1,1,0,1,1,0,1]
    la fonction(tableau, 0) doit renvoyer "0, 4, 7" (use first func lol!)
"""
def occurance1(list, val):
    result = ""

    # Pour i prend toutes les valeurs entre 0 à la longueur de list - 1
    for i in range(len(list)):
        # Si l'element numero i est égal a val,
        if list[i] == val:
            # Alors concatener ret avec l'index
            result = concat(result, str(i))
    
    # A la fin de la boucle, return result sans les deux premiers caracteres, donc enlever ", " au debut
    return result[2:]
# OU
def occurance2(list, val):
    # Definir result en tant que string vide
    result = ""

    # Pour i prend toutes les valeurs entre 0 à la longueur de list - 1
    for i in range(len(list)):
        # Si l'element numero i est égal a val,
        if list[i] == val:
            if result == "": # Si ret est une chaine de caractere vide,
                # Alors le redefinir en tant que l'index trouvé
                result = str(i)
            else: # Sinon,
                # Concatener ret avec l'index
                result = concat(result, i)
    
    # A la fin de la boucle, return result
    return result
# OU
def occurance3(list, val):
    # Initialiser i a 0
    i = 0
    # Initialiser isFirstFound a vrai
    isFirstFound = True
    # Definir chaineResultat en tant que 
    chaineResultat = str()

    # Tant que i est inferieur que la longueur de la liste
    while i < len(list):
        # Si l'élement d'index i dans la liste est égal a val
        if list[i] == val:
            # Alors

            # Si isFirstFound est vrai
            if isFirstFound:
                # Alors on assigne chaineResultat a str(val)
                chaineResultat = str(i)
                # On assigne faux a isFirstFound
                isFirstFound = False
            else:
                # Sinon on assigne chaineResultat le retour de concat(chaineResultat, str(i))
                chaineResultat = concat(chaineResultat, str(i))
        # On incremente i de 1
        i += 1
    # Renvoyer chaineResultat
    return chaineResultat

print(occurance3([0,1,1,1,0,1,1,0,1], 0))

"""
Exercice 3:
    Faire une fonction Afficher un message
"""
def msg(x):
    print(f'[MESSAGE] {x}')

"""
Exercice 4:
    Tel que
"""
users = {
    "Alex": "mdp",
    "evn": "pw",
    "rayouyou": "12345",
    "gwen": "azerty"
}
"""
    Ecrire la fonction login(userName, password, userInfo) permettant d'afficher
    un message de connextion si le combo user/ppw est bon
"""
def login(userName, password, userInfo):
    # Trouver l'utilisateur
    # Si userName n'est pas dans userInfo, userPassword sera vide
    userPassword = userInfo.get(userName)

    # Renvoyer l'égalité entre userPassword et password
    # si le MDP est juste, alors True, sinon False
    return userPassword == password

if login(input('Username: '), input('Password: '), users):
    print("Login sucessful!")
else:
    print("Login failed!")