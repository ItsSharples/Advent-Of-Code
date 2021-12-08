from collections import defaultdict, Counter

with open("Day 8/Day8", "r") as file:
    vectors = [list(map(str.split, line.split("|"))) for line in file.read().splitlines()]

# Usage Map for 2,3,5,6,9,0
#  66
# 4  4
# 4  4
#  55
# 3  5
# 3  5
#  66

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
    "abcefg"    : '0'}

# Part 1
outputs = [x for vec in vectors for x in vec[1]]
lengths = Counter([len(o) for o in outputs])
totalCount = sum([lengths[2], lengths[3], lengths[4], lengths[7]])
# Part 2
finalAnswer = 0
for input, output in vectors:
    unknowns = ""
    sevenSegments: str
    # For this we only need the segments for 7, and the other unknowns (1,4,8 are known by length)
    for signal in input:
        match len(signal):
            case 2 | 4 | 7: None
            case 3: sevenSegments = signal
            case _: unknowns += signal
    # Then we can use the usage count for each segment to find which segment lines up where
    lookupSegments = defaultdict(str)
    for pair in {
            counts: [char for char in set(unknowns) if Counter(unknowns)[char] == counts]
            for counts in [3,4,5,6]
            }.items():
        # True is higher than False. Only one will be True, and One False
        values = sorted(pair[1], key=lambda x: x in sevenSegments, reverse=True)
        match pair[0]:
            # Unpack command but only one item, very cursed
            case 3: lookupSegments["e"],                     = values
            case 4: lookupSegments["c"], lookupSegments["b"] = values
            case 5: lookupSegments["f"], lookupSegments["d"] = values
            case 6: lookupSegments["a"], lookupSegments["g"] = values
    # Flip key, value because we're translating the other direction
    translation = str.maketrans({value:key for key, value in lookupSegments.items()})
    finalAnswer += int(''.join(map(lambda disp: numbers[''.join(sorted(disp.translate(translation)))], output)))
    
print(f"Part 1: {totalCount}")
print(f"Part 2: {finalAnswer}")