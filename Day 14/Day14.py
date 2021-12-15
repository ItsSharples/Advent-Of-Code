from collections import defaultdict, Counter
from copy import copy
import concurrent.futures
from os import error

with open("Day 14/Day14", "r") as file:
    pairs = file.read().split('\n\n')
    data, instructions = pairs

polymerTable = defaultdict(str)
polymerTableEdit = defaultdict(tuple[str, str])
counting = {}
for instruction in instructions.splitlines():
    requires, inserts = instruction.split(" -> ")
    polymerTable[requires] = inserts
    polymerTableEdit[requires] = (requires[0] + inserts, inserts + requires[1])
    counting[inserts] = 0

lookup = defaultdict(defaultdict)
def getChunkAfterStep(chunk: str, step: int, counter: Counter):
    if not lookup[step]:
        lookup[step] = defaultdict()
    if lookup[step].get(chunk, None) == None:
        lookup[step][chunk] = getChunkAfterStepInternal(chunk, step, counter)
    return lookup[step][chunk]

def getChunkAfterStepInternal(chunk: str, step: int, counter: Counter):
    if step == 0:
        return Counter(chunk)
    else:
        a,b = polymerTableEdit[chunk]

        if step == 1: return counter + getChunkAfterStep(b, step-1, counter)
        else:
            return getChunkAfterStep(a, step-1, counter) + getChunkAfterStep(b, step-1, counter)

data = list(data)
def task(numSteps: int) -> Counter:
    out = Counter()
    for i in range(len(data)):
        chunk = "".join(data[i:i+2])
        if len(chunk) == 2:
            out += getChunkAfterStep(chunk, numSteps, Counter())
    return out

#part 1
sorted = task(10).most_common()
most, least = sorted[0], sorted[-1]
print(most[1] - least[1])
#part 2
sorted = task(40).most_common()
most, least = sorted[0], sorted[-1]
print(most[1] - least[1])

print(sum(map(lambda step: lookup[step].__len__(), range(40))))