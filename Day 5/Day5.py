from math import gcd
from collections import Counter
class Vector:

    def __init__(self, line) -> None:
        # Convert x1,y1 -> x2,y2 to data
        start, dest = line.split(" -> ")
        (x1,y1) = start.split(',')
        (x2,y2) = dest.split(',')
        x1,x2,y1,y2 = int(x1), int(x2), int(y1), int(y2)
        self.start = (x1, y1)
        (self.minX, self.maxX) = (x1, x2) if x1 < x2 else (x2, x1)
        (self.minY, self.maxY) = (y1, y2) if y1 < y2 else (y2, y1)
        

        if x1 == x2:
            self.locations = [[self.minY, x] for x in range(self.minX, self.maxX + 1)]
            return
        if y1 == y2:
            self.locations = [[y, self.minX] for y in range(self.minY, self.maxY + 1)]
            return 

        diagonal = (x2 - x1, y2 - y1)
        self.diagonalCount = abs(gcd(*diagonal))
        self.diagonal = list(map(lambda x: int(int(x)/self.diagonalCount), diagonal))
        self.locations = [[self.start[0] + self.diagonal[0] * d, self.start[1] + self.diagonal[1] * d] for d in range(self.diagonalCount + 1)]
        
        

    def editMap(self, map):
        for location in self.locations:
            print(location)
            a = map[location[0]]
            b = a[location[1]]
            print(b)
            #[location[1]] += 1

def getFileLines(filename):
    with open(filename, "r") as file:
        return file.read().splitlines()


data = getFileLines("Day 5/Day5")

vectors = []
Min = (9999,9999)
Max = (0,0)
for line in data:
    vector = Vector(line);
    vectors.append(vector)

    Min = (min(vector.minX, Min[0]), min(vector.minY, Min[1]))
    Max = (max(vector.maxX, Max[0]), max(vector.maxY, Max[1]))


mapmap = [[0] * (Max[0] + 1) for x in range(Max[1] + 1)]
for vector in vectors:
    mapmap = vector.editMap(mapmap)

out = sum([sum([1 if x > 1 else 0 for x in y]) for y in mapmap])
print(out)