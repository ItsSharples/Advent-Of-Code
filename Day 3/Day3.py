import operator
from copy import deepcopy

showGamma = True
class Rate:
    def __init__(self):
        self.lowCount = 0
        self.highCount = 0

    def low(self):
        self.lowCount += 1
    def high(self):
        self.highCount += 1

    @property
    def gamma(self):
        return 0 if (self.lowCount > self.highCount) else 1
    @property
    def epsilon(self):
        return 0 if (self.lowCount < self.highCount) else 1

    def __repr__(self) -> str:
        return str(self.gamma if showGamma else self.epsilon)

def joinList(iterable):
    return ("".join([str(iter) for iter in iterable]))


with open("Day 3/Day3", "rb") as file:
    data = file.read().splitlines()
    rates = [Rate() for x in range(len(data[0]))]

    for line in data:
        for i, col in enumerate(line):
            rates[i].high() if (col - 48) else rates[i].low()

    showGamma = True
    gamma = joinList(rates)
    showGamma = False
    epsilon = joinList(rates)

    print((int(gamma, base=2)) * int(epsilon, base = 2))


with open("Day 3/Day3", "rb") as file:
    data = file.read().splitlines()
    column = [[int(chr(col)) for col in line] for line in data]
    flipped = list(zip(*column))
    highIsCommon = map(lambda col: int(sum(col) >= (len(col) / 2.0)), flipped)
    lowIsCommon = map(lambda col: int(sum(col) < (len(col) / 2.0)), flipped)
    gamma = joinList(highIsCommon)
    epsilon = joinList(lowIsCommon)
    print((int(gamma, base=2)) * int(epsilon, base = 2))

with open("Day 3/Day3", "rb") as file:
    highIsCommon = list(map(lambda col: int(sum(col) >= (len(col) / 2.0)), list(zip(*[[int(chr(col)) for col in line] for line in file.read().splitlines()]))))
    print((int("".join(["1" if item else "0" for item in highIsCommon]), 2)) * int("".join(["0" if item else "1" for item in highIsCommon]), 2))

# Part 2
with open("Day 3/Day3", "rb") as file:
    data =  file.read().splitlines()

# data = [
# b'00100',
# b'11110',
# b'10110',
# b'10111',
# b'10101',
# b'01111',
# b'00111',
# b'11100',
# b'10000',
# b'11001',
# b'00010',
# b'01010'
# ]

column = [[int(chr(col)) for col in line] for line in data]

def flip(data) -> list:
    return list(zip(*data))

def findBestFit(data: column, findHigh: bool = True):
    notFound = True
    index: int = 0
    while notFound:
        col = flip(data)[index]
        highIsCommon = (sum(col) >= (len(col) / 2.0))
        searchFor = not operator.xor(findHigh, highIsCommon)
        new = list(filter(lambda x: x[index] == searchFor, data))
        if len(new) < 2:
            return new[0]
        data = new
        index += 1

oxygen = (int(joinList(findBestFit(deepcopy(column), True)), base=2))
cot = (int(joinList(findBestFit(deepcopy(column), False)), base=2))

print(oxygen * cot)
