from collections import defaultdict, Counter
from copy import deepcopy
from threading import Thread

with open("Day 14/Example", "r") as file:
    pairs = file.read().split('\n\n')
    data, instructions = pairs

polymerTable = defaultdict(str)
polymerTableEdit = defaultdict(str)
for instruction in instructions.splitlines():
    requires, inserts = instruction.split(" -> ")
    polymerTable[requires] = inserts
    polymerTableEdit[requires] = requires[0] + inserts + requires[1]

data = list(data)
numSteps = 10


difference = [0]
dataCopy = list(data)
for i in range(len(data)):
    chunk = "".join(data[i:i+2])
    if chunk in polymerTable.keys():
        for step in range(numSteps):
            newChunk = polymerTableEdit[chunk]
data = "".join(dataCopy)

    sortedData = Counter(data).most_common()
    mostCommon, leastCommon = sortedData[0], sortedData[-1]
    ans = (mostCommon[1] - leastCommon[1])
    difference.append(ans - difference[-1])
    print(step, ans, difference)

print("Complete Work")
sortedData = Counter(data).most_common()
mostCommon, leastCommon = sortedData[0], sortedData[-1]
print(mostCommon[1] - leastCommon[1])
print(sum(difference[-2:]))