



from collections import defaultdict
from typing import Counter, Set

class Signal:

    def __init__(self, value) -> None:
        match len(value):
            case 2: out = 1
            case 3: out = 7
            case 4: out = 4
            case 7: out = 8
            case _: out = 99
        self.value = out


with open("Day 8/Day8", "r") as file:
    vectors = [list(map(str.split, line.split("|"))) for line in file.read().splitlines()]

outputs = [x for vec in vectors for x in vec[1]]
lengths = Counter(outputs)



segments = {
    "a" : [2,3,5,6,7,8,9,0],
    "b" : [4,5,6,8,9,0],
    "c" : [1,2,3,4,6,7,8,9,0],
    "d" : [2,3,4,5,6,8,9],
    "e" : [2,6,8,0],
    "f" : [1,3,4,5,6,7,8,9],
    "g" : [2,3,5,6,8,9,0]
}

numbers = {
    "cf"        : '1',
    "acdeg"     : '2',
    "acdfg"     : '3',
    "bcdf"      : '4',
    "abdfg"     : '5',
    "abdefg"    : '6',
    "acf"       : '7',
    "abcdefg"   : '8',
    "abcdfg"    : '9',
    "abcefg"    : '0'
}

charsInAll = set(list("abcdefg"))

finalAnswer = 0
for input, output in vectors:
    lookupNumbers = defaultdict(str)
    lookupSegments = defaultdict(str)
    unknowns = []
    for signal in input:
        match len(signal):
            case 2: lookupNumbers[1] = list(signal)
            case 3: lookupNumbers[7] = list(signal)
            case 4: lookupNumbers[4] = list(signal)
            case 7: lookupNumbers[8] = list(signal)
            case _: unknowns.append(signal)

    count = Counter("".join(unknowns))
    sevenSegments: list[str] = lookupNumbers[7]
    vals = defaultdict(list)
    for item in count.items():
        vals[item[1]].append(item[0])
    for pair in vals.items():
        values: list[str] = pair[1]
        rValues = list(reversed(values))
        match pair[0]:
            case 3:
                lookupSegments["e"] = values[0]
            case 4:
                lookupSegments["b"], lookupSegments["c"] = values if values[1] in sevenSegments else rValues
            case 5:
                lookupSegments["d"], lookupSegments["f"] = values if values[1] in sevenSegments else rValues
            case 6:
                lookupSegments["g"], lookupSegments["a"] = values if values[1] in sevenSegments else rValues
    # ag = list(map(lambda pair: pair[0], filter(lambda pair: pair[1] == 6, count.items())))
    # df = list(map(lambda pair: pair[0], filter(lambda pair: pair[1] == 5, count.items())))
    # bc = list(map(lambda pair: pair[0], filter(lambda pair: pair[1] == 4, count.items())))

    # lookupSegments["e"] = list(filter(lambda pair: pair[1] == 3, count.items()))[0][0]

    # if ag[0] in lookupNumbers[7]:
    #     lookupSegments["a"], lookupSegments["g"] = ag
    # else:
    #     lookupSegments["g"], lookupSegments["a"] = ag

    # if df[1] in lookupNumbers[7]:
    #     lookupSegments["d"], lookupSegments["f"] = df
    # else:
    #     lookupSegments["f"], lookupSegments["d"] = df

    # if bc[1] in lookupNumbers[7]:
    #     lookupSegments["b"], lookupSegments["c"] = bc
    # else:
    #     lookupSegments["c"], lookupSegments["b"] = bc

    # lookupNumbers[2] = [lookupSegments["a"], lookupSegments["c"], lookupSegments["d"], lookupSegments["e"], lookupSegments["g"]]
    # lookupNumbers[3] = [lookupSegments["a"], lookupSegments["c"], lookupSegments["d"], lookupSegments["f"], lookupSegments["g"]]
    # lookupNumbers[5] = [lookupSegments["a"], lookupSegments["b"], lookupSegments["d"], lookupSegments["f"], lookupSegments["g"]]
    # lookupNumbers[6] = [lookupSegments["a"], lookupSegments["b"], lookupSegments["d"], lookupSegments["e"], lookupSegments["f"], lookupSegments["g"]]
    # lookupNumbers[9] = [lookupSegments["a"], lookupSegments["b"], lookupSegments["c"], lookupSegments["d"], lookupSegments["f"], lookupSegments["g"]]
    # lookupNumbers[0] = [lookupSegments["a"], lookupSegments["b"], lookupSegments["c"], lookupSegments["e"], lookupSegments["f"], lookupSegments["g"]]
    
    translation = str.maketrans({value:key for key, value in lookupSegments.items()})

    print(translation)
    # sortedNumbers = {}
    # for key, value in lookupNumbers.items():
    #     sortedNumbers[key] = "".join(sorted(value))

    # print(lookupSegments)
    # print(sortedNumbers)

    # display = []
    # for disp in output:
    #     sortedDisp = "".join(sorted(list(disp)))
    #     success = False
    #     for key, value in sortedNumbers.items():
    #         if value == sortedDisp:
    #             display.append(key)
    #             success = True
    #     if not success:
    #         print(sortedDisp)
        
    # print(display)
    # print
        

    finalAnswer += int(''.join(map(lambda disp: numbers[''.join(sorted(disp.translate(translation)))], output)))
    
print(finalAnswer)