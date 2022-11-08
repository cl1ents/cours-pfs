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
def concat(a, b):
    return a + ", " + b

"""
Exercice 2:
    Faire une fonction qui itere sur tous les index d'un tableau renvoyant une chaine de
    caractere avec l'ensemble des occuration d'un chiffre
    e.g.: Pour tableau [0,1,1,1,0,1,1,0,1]
    la fonction(tableau, 0) doit renvoyer "0, 4, 7" (use first func lol!)
"""
def occurance1(list, val):
    ret = ""

    # Pour i prend toutes les valeurs entre 0 à la longueur de list - 1
    for i in range(len(list)):
        # Si l'element numero i est égal a val,
        if list[i] == val:
            # Alors concatener ret avec l'index
            ret = concat(ret, str(i))
    
    # A la fin de la boucle, return ret sans les deux premiers caracteres, donc enlever ", " au debut
    return ret[2:]
# OU
def occurance2(list, val):
    ret = ""

    # Pour i prend toutes les valeurs entre 0 à la longueur de list - 1
    for i in range(len(list)):
        # Si l'element numero i est égal a val,
        if list[i] == val:
            if ret == "": # Si ret est une chaine de caractere vide,
                # Alors le redefinir en tant que l'index trouvé
                ret = str(i)
            else: # Sinon,
                # Concatener ret avec l'index
                ret = concat(ret, str(i))
    
    # A la fin de la boucle, return ret
    return ret

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