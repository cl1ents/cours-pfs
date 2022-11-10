# DEBUT

from random import randint, seed

## INITIAL VALUES

directions = [
    (1,0),
    (-1,0),
    (0,1),
    (0,-1),
]

## FUNCTIONS

"""
Creates grid of X by X
"""
def createGrid(X):
    result = []
    for _ in range(X):
        result.append([randint(0,1) for _ in range(X)])
    return result

"""
Displays the grid in a clean way in the console
"""
def printGrid(grid):
    for row in grid:
        for element in row:
            print(element, end=" ")
        print()

"""
merci alex
"""
def displayGrid(grid):
    for i in grid:
        print(i)


def testCoordinate(grid, x, y):
    return x >= 0 and y >= 0 and x < len(grid) and y < len(grid[x]) 

def getTouchingDirection(grid, x, y):
    result = []
    for direction in directions:
        if testCoordinate(grid, x+direction[0], y+direction[1]):
            result.append(direction)
    return result

def getTouchingCoordinates(grid, x, y):
    touchingDirections = getTouchingDirection(grid, x, y)
    return [(x+direction[0], y+direction[1]) for direction in touchingDirections]

def getTouchingElements(grid, x, y):
    touchingCoordinates = getTouchingCoordinates(grid, x, y)
    return [grid[coordinate[0]][coordinate[1]] for coordinate in touchingCoordinates]

def getTouchingValues(grid, x, y):
    print()

def showTouchingCoodrinates(grid, x, y):
    touchingDirections = getTouchingDirection(grid, x, y)
    touchingElements = getTouchingElements(grid, x, y)
    toDisplay = [
        [' ', ' ', ' '],
        [' ', grid[x][y], ' '],
        [' ', ' ', ' ']
    ]

    for i in range(len(touchingDirections)):
        toDisplay[1+touchingDirections[i][0]][1+touchingDirections[i][1]] = touchingElements[i]

    printGrid(toDisplay)

## RUNTIME

## SET THE SEED TO GET A "FIXED" GRID!
seed(1)
grid = createGrid(10)

printGrid(grid)

print(getTouchingCoordinates(grid, 0, 5))
showTouchingCoodrinates(grid, 0, 5)

# FIN