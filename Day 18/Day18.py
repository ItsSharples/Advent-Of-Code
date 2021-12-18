from itertools import permutations
from Commands import *


def getMagnitudeForInput(input: list[list]):
    

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
#     lstPair = [input[indexPair[0]], input[indexPair[1]]]
#     maxValue = max(getMagnitudeForInput(lstPair), maxValue)
# print(maxValue)
