from functools import reduce
from statistics import median

data: list[list[str]]
with open("Day 10/Day10", "r") as dataFile:
    data = [[str(item) for item in line] for line in dataFile.read().splitlines()]

corruptedScores = {
    ")" : 3,
    "]" : 57,
    "}" : 1197,
    ">" : 25137,
}

completeScores = {
    ")" : 1,
    "]" : 2,
    "}" : 3,
    ">" : 4,
}

badChars = []
autoCompleteScores = []
for line in data:
    expectedChar = []
    for char in line:
        match char:
            case "(": expectedChar.append(")")
            case "[": expectedChar.append("]")
            case "{": expectedChar.append("}")
            case "<": expectedChar.append(">")
            case _: # The Closes
                compare = expectedChar.pop()
                if char != compare:
                    badChars.append(char)
                    expectedChar = []
                    break

    autoCompleteScores.append(reduce(lambda partial, value: (partial * 5) + completeScores[value], expectedChar.__reversed__(), 0))


print(f"Part 1:{sum(map(lambda x: corruptedScores[x], badChars))}")
print(f"Part 2:{median([i for i in autoCompleteScores if i != 0])}")