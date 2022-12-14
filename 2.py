def assertionUn(r, s, e, rh):
    return (((365 * 3) / (24 - ( 16 - 8))) * (rh) > r) == (e * s < r)

"""
Calcul du salaire par seconde avec:
- Le salaire par heures,
- Le nombre d'heure par jours ouvrables,
- Le nombre de jours ouvrables dans l'année
"""
def salaireParSecondeSurUnAn(salaireParHeure, heureParJourOuvrable, joursOuvrables):
    #      (                     salaire Annuel                    ) / (Secondes/an)
    return (salaireParHeure * heureParJourOuvrable * joursOuvrables) / (365*24*60*60)

"""
Salaire NET d'un salaire BRUTE
"""
def calculNet(salaireBrute, public):
    # Si j'occupe un poste de la fonction publique (si public est vrai), alors pourcentage = 15%, sinon pourcentage = 23%
    pourcentage = .15 if public else .23
    # return le salaire avec le pourcentage soustrait
    return salaireBrute - (salaireBrute * pourcentage)

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    # Si Y est 0, la division est impossible
    if y == 0:
        # Alors afficher un message d'erreur
        print("ERR: Can't divide by 0!")
        # Et return rien
        return 
    # Sinon, continuer normalement
    return x / y

def mod(x, y):
    return x % y

#-------------------------------------------#

"""
Je sais que c'est une très mauvaise pratique.
"""
def X(text):
    i = input(text)
    if i == "":
        return 0
    return eval(i)

#-------------------------------------------#

print('-- assertionUn --')
print(assertionUn(X('r: '), X('s: '), X('e: '), X('rh: ')))

print('-- salaireParSecondeSurUnAn --')
print(salaireParSecondeSurUnAn(X('Le salaire par heures: '), X('Le nombre d\'heure par jours ouvrables: '), X('Le nombre de jours ouvrables dans l\'année: ')))

print('-- calculNet --')
print(calculNet(X('Le salaire NET: '), X('Fonction publique? (true/false): ')))

print('-- add --')
print(add(X('x: '), X('y: ')))

print('-- sub --')
print(sub(X('x: '), X('y: ')))

print('-- mult --')
print(mult(X('x: '), X('y: ')))

print('-- div --')
print(div(X('x: '), X('y: ')))

print('-- mod --')
print(mod(X('x: '), X('y: ')))