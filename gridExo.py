# DEBUT

from random import randint, seed
from time import sleep
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


## INITIAL VALUES

directions = [
    (1,0),
    (1,1),
    (1,-1),
    
    (-1,0),
    (-1,1),
    (-1,-1),

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
        result.append([randint(0, 1) for _ in range(X)])
    return result

"""
Displays the grid in a clean way in the console
"""
def printGrid(grid):
    display = '\n'*10
    for row in grid:
        display+='\n'
        for element in row:
            display += "⬜" if element else "⬛"
    print(display, end = "")

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

def conwayTick(grid):
    newGrid = []
    for x in range(len(grid)):
        row = grid[x]
        newRow = []
        for y in range(len(row)):
            element = row[y]
            newElement = 0
            touchingElements = getTouchingElements(grid, x, y)
            count = sum(touchingElements)
            if count == 2 and element == 1:
                newElement = 1
            elif count == 3:
                newElement = 1
            newRow.append(newElement)
        newGrid.append(newRow)
    return newGrid

## RUNTIME

## SET THE SEED TO GET A "FIXED" GRID!
# seed(1)
grid = createGrid(100)

"""
printGrid(grid)

print(getTouchingCoordinates(grid, 5, 5))
showTouchingCoodrinates(grid, 5, 5)
"""
while True:
    printGrid(grid)
    grid = conwayTick(grid)
    sleep(.2)

# FIN