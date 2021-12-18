from Commands import *



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
