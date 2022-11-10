def concat(chaineA, chaineB):
    # Assurer qu'ils sont des str
    # (Changer le type de a et de b en string)
    stringifiedChaineA = str(chaineA)
    stringifiedChaineB = str(chaineB)
    # Retourner 
    return stringifiedChaineA + ", " + stringifiedChaineB

def joinWithComma(list):
    first = True
    result = ''
    for value in list:
        if first:
            result = str(value)
            first = False
        else:
            result = concat(result, value)
    return result

# On definie une fonction `fibonacci` qui prend pour argument "length"
# qui correspondera a la longueure de la suite donnée
def fibonacci(length):
    # Definir une liste `fibonacciList` avec 0 et 1 comme éléments initiaux.
    fibonacciList = [0, 1]

    # Enlever 2 a la valeur `length`
    length = length - 2
    # Si length est plus petit que 0,
    if length < 0:
        # Alors renvoyer une liste avec simplement [0] dedans
        return [0]
    
    # Pour i prenant toutes les valeurs entre 0 et length-1
    for i in range(length):
        # Ajouter a la fin de la liste `fibonacciList` la somme entre le dernier et l'avant dernier élément dans `fibonacciList`
        fibonacciList.append(fibonacciList[-2] + fibonacciList[-1])
    
    return joinWithComma(fibonacciList)

print(fibonacci(10))