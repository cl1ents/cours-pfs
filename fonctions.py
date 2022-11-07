def assertionUn(r, s, e, rh):
    return (((365 * 3) / (24 - ( 16 - 8))) * (rh) > r) == (e * s < r)

def add(x, y):
    return x + y

def sub(x, y):
    return x + y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y

def mod(x, y):
    return x % y

"""
Calcul du salaire par seconde avec:
- Le salaire par heures,
- Le nombre d'heure par jours ouvrables,
- Le nombre de jours ouvrables dans l'année
"""
def salaireParSecondeSurUnAn(salaireParHeure, heureParJourOuvrable, joursOuvrables):
    return (salaireParHeure * heureParJourOuvrable * joursOuvrables) / 31536000

"""
Salaire NET d'un salaire BRUTE
"""
def calculNet(salaireBrute):
    return salaireBrute - (salaireBrute * .23)

"""
Je sais que c'est une très mauvaise pratique.
"""
def X(text):
    return eval(input(text))

print('-- assertionUn --')
print(assertionUn(X('r: '), X('s: '), X('e: '), X('rh: ')))

print('-- salaireParSecondeSurUnAn --')
print(salaireParSecondeSurUnAn(X('Le salaire par heures: '), X('Le nombre d\'heure par jours ouvrables: '), X('Le nombre de jours ouvrables dans l\'année: ')))

print('-- calculNet --')
print(calculNet(X('Le salaire NET: ')))

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