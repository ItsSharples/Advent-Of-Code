from copy import copy, deepcopy
from math import floor, ceil
from itertools import permutations

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

doTests = False
if doTests:
    test = eval("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]")
    at    = (0, 1, 1, 1, 0)
    left  = (0, 1, 1, 0, 0)
    right = (1, 0, 0, 0, 0)

    print("Get Child Close To")
    print(getChildCloseTo(test, at))
    print(getChildCloseTo(test, left))
    print(getChildCloseTo(test, right))
    print("Get Closest Coords To")
    print(getClosestCoordsTo(test, at))
    print(getClosestCoordsTo(test, left))
    print(getClosestCoordsTo(test, right))
    print("Increment Test")
    print(incrementCoord(test, at))
    print(incrementCoord(test, left))
    print(incrementCoord(test, right))
    print("Decrement Test")
    print(decrementCoord(test, at))
    print(decrementCoord(test, left))
    print(decrementCoord(test, right))
    print("Should Explode test")
    print(shouldExplode(test, at))
    print(shouldExplode(test, left))
    print(shouldExplode(test, right))
    print("Should Split test")
    print(shouldSplit(test, at))
    print(shouldSplit(test, left))
    print(shouldSplit(test, right))
    print("Split Test")
    print(10, splitItem(10))
    print(11, splitItem(11))
    print(12, splitItem(12))
    print(15, splitItem(15))
    print("Add List Test")
    print(addLists([1,[2,[3,4]]], [5,[6]]))
    # print("Non Mutating Edit test")
    # print(makeNewParentWithChild(test, at, 10))
    # print(makeNewParentWithChild(test, left, 10))
    # print(makeNewParentWithChild(test, right, 10))
    # print("Mutating Edit test")
    # print(updateChildCloseTo(test, at, 10))
    # print(updateChildCloseTo(test, left, 10))
    # print(updateChildCloseTo(test, right, 10))

    print("Finish Tests")

def getMagnitudeForInput(input: list[list]):
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

    state = input[0]
    for newList in input[1:]:
        state = addLists(state, newList)

        toExplode, toSplit = searchCoords(state)
        while True:
            while toExplode:
                coord = toExplode[0]

                explodeList = getListForCoords(state, coord)
                
                leftCoord = padToMatch(explodeList + [0], coord)
                rightCoord = padToMatch(explodeList + [1], coord)
                
                left = [decrementCoord(state, leftCoord), leftCoord]
                right = [incrementCoord(state, rightCoord) + [1], rightCoord]

                leftSum = sum([getChildCloseTo(state, item) for item in left])
                rightSum = sum([getChildCloseTo(state, item) for item in right])

                updateChildCloseTo(state, left[0], leftSum)
                updateChildCloseTo(state, right[0], rightSum)
                updateChildCloseTo(state, explodeList, 0)

                toExplode, toSplit = searchCoords(state)

            # print(state, toExplode, toSplit)
            if toSplit:
                coord = toSplit[0]
                value, at = getChildAndCoordsCloseTo(state, coord)
                updateChildCloseTo(state, at, splitItem(value))
                toExplode, toSplit = searchCoords(state)
            else:
                if not toExplode: break
    #         print(state, toExplode, toSplit)
        
    # print(state)


    coord = [0] * 10

    exploded = False
    def getChild(state):
        if isinstance(state[0], list):
            left = getChild(state[0])
        else:
            left = state[0]

        if isinstance(state[1], list):
            right = getChild(state[1])
        else:
            right = state[1]

        return 3*left + 2*right

    return getChild(state)


with open("Day 18/Example", "r") as file:
    data = file.read()
    
    strInput = [line for line in data.splitlines()]
    input = [eval(line) for line in data.splitlines()]

maxValue = 0
for pair in list(permutations(strInput, 2)):
    # Exploiting that '[]' is a valid python statement
    # Doing this in the file input seems to fuck up inside of 'permutations'
    maxValue = max(getMagnitudeForInput([eval(pair[0]), eval(pair[1])]), maxValue)
print(maxValue)

# maxValue = 0
# for indexPair in list(permutations(range(len(input)), 2)):
#     # Exploiting that '[]' is a valid python statement
#     # Doing this in the file input seems to fuck up inside of 'permutations'
#     lstPair = [input[indexPair[0]], input[indexPair[1]]]
#     maxValue = max(getMagnitudeForInput(lstPair), maxValue)
# print(maxValue)
