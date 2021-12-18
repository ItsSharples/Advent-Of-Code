from copy import copy, deepcopy
from math import floor

def getChildCloseTo(parent: list, coords: list) -> int | list:
    child = copy(parent)
    i = 0
    while isinstance(child, list) and len(coords) > i:
        child: int | list = child[coords[i]]
        i+=1
    return child

def getChildAndCoordsCloseTo(parent: list, coords: list) -> int | list:
    child = copy(parent)
    i = 0
    while isinstance(child, list) and len(coords) > i:
        child: int | list = child[coords[i]]
        i+=1
    return child, coords[:i]

def updateChildCloseTo(parent: list, coords: list, newValue: int):
    child, closeCoords = getChildAndCoordsCloseTo(parent, coords)
    if child == newValue: return parent

    # This is jank but I'm lazy
    match(len(closeCoords)):
        case(1): parent[closeCoords[0]] = newValue
        case(2): parent[closeCoords[0]][closeCoords[1]] = newValue
        case(3): parent[closeCoords[0]][closeCoords[1]][closeCoords[2]] = newValue
        case(4): parent[closeCoords[0]][closeCoords[1]][closeCoords[2]][closeCoords[3]] = newValue
        case(5): parent[closeCoords[0]][closeCoords[1]][closeCoords[2]][closeCoords[3]][closeCoords[4]] = newValue
        case(6): parent[closeCoords[0]][closeCoords[1]][closeCoords[2]][closeCoords[3]][closeCoords[4]][closeCoords[5]] = newValue
    return parent

def makeNewParentWithChild(parent: list, coords: list, newValue: int):
    return updateChildCloseTo(deepcopy(parent), coords, newValue)

def getClosestCoordsTo(parent: list, coords: list):
    child = copy(parent)
    i = 0
    while isinstance(child, list) and len(coords) > i:
        child = child[coords[i]]
        i+=1
    return tuple(coords[j] for j in range(len(coords)) if j < i)

def incrementCoord(parent: list, coords: list):
    '''Increment Coord, while maintaining fitness to the parent, and the original dimensions.
    If new coord exceeds the parent bounds, returns original coords'''
    child = copy(parent)
    childLens = []
    i = 0
    while len(coords) > i:
        if isinstance(child, list):
            childLens.append(len(child))
            child = child[coords[i]]
        else:
            # We fill out the rest of the coords as 0,
            #   because they're not lists
            childLens.append(0)
        i+=1
    # Always try and go one deeper
    childLens.append(0)
    # Start at the end going in
    outCoords = list(coords)
    outCoords = padToMatch(outCoords, childLens)
    index = len(outCoords) - 1
    outCoords[index] += 1
    # print(index, childLens)
    while outCoords[index] >= childLens[index]:
        outCoords[index] = 0
        index -= 1
        if index < 0: return list(coords)
        outCoords[index] += 1
    return outCoords

def decrementCoord(parent: list, coords: list):
    '''Decrement Coord, while maintaining fitness to the parent, and the original dimensions.
    If new coord exceeds the parent bounds, returns original coords'''
    child = copy(parent)
    childLens = []
    i = 0
    while len(coords) > i:
        if isinstance(child, list):
            childLens.append(len(child))
            child = child[coords[i]]
        else:
            # We fill out the rest of the coords as 0,
            #   because they're not lists
            childLens.append(0)
        i+=1
    outCoords = list(coords)
    outCoords = padToMatch(outCoords, childLens)
    index = len(outCoords) - 1
    while outCoords[index] == 0:
        index -= 1
        # It's all zeros, stop caring
        if index < 0: return outCoords

    outCoords[index] -= 1
    # Now we have to wraparound all the following indices 
    for j in range(index + 1, len(outCoords)):
        value = childLens[j] - 1
        if value < 0: value = 0
        outCoords[j] = value
    return outCoords

def shouldExplode(parent: list, coords: list):
    child = copy(parent)
    i = 0
    while isinstance(child, list) and len(coords) > i:
        child = child[coords[i]]
        i+=1
        if i > 4: return True
    return False

def getDepth(parent: list, coords: list):
    child = copy(parent)
    i = 0
    while isinstance(child, list) and len(coords) > i:
        child = child[coords[i]]
        i+=1
    return i

def getListForCoords(parent: list, coords: list):
    # print(coords)
    while isinstance(getChildCloseTo(parent, coords), int):
        coords = coords[:-1]
    return coords

def shouldSplit(parent: list, coords: list):
    child = getChildCloseTo(parent, coords)
    if isinstance(child, list): return False
    return child >= 10

def splitItem(item: int) -> list:
    left = floor(item / 2)
    return [left, item - left]

def addLists(left: list, right: list):
    out = []
    out.append(left)
    out.append(right)
    return out

def padToMatch(pad: list, match: list):
    return pad + [0] * (len(match) - len(pad))

def searchCoords(state: list) -> tuple[list, list]:
        coord = [0] * 10
        toExplode = []
        toSplit = []
        exploded = False
        while incrementCoord(state, coord) != coord:
            if shouldExplode(state, coord): toExplode.append(coord)
            if shouldSplit(state, coord): toSplit.append(coord)
            coord = incrementCoord(state, coord)
        
        if shouldExplode(state, coord): toExplode.append(coord)
        if shouldSplit(state, coord): toSplit.append(coord)

        return toExplode[::2], toSplit
