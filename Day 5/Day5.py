from math import gcd, copysign
from typing import List

class Vector:
    def __init__(self, line) -> None:
        # Convert 'x1,y1 -> x2,y2' to x1, y1, x2, y2
        (x1,y1), (x2,y2) = (map(int, pair) for pair in (point.split(',') for point in line.split(" -> ")))
        
        diagonal = (x2 - x1, y2 - y1)
        divisor = abs(gcd(*diagonal))
        lerp = lambda a, b, t : tuple(a[i] + b[i] * t for i in range(2))
        step = [int(diagonal[i]/divisor) for i in range(2)]

        self.isDiagonal = not (x1 == x2 or y1 == y2)
        self.locations = [ lerp((x1, y1), step, d) for d in range(divisor + 1)]

    def overdrawMatrix(self, matrix: "list[list[int]]", useDiagonals = True) -> "list[list[int]]" :
        if (not useDiagonals) and self.isDiagonal:
            return matrix
        
        for location in vector.locations:
            matrix[location[0]][location[1]] += 1
        
        return matrix
    
findOverlap = lambda matrix: [1 if x > 1 else 0 for y in mapmap for x in y ]

with open("Day 5/Day5", "r") as file:
    vectors = [Vector(line) for line in file.read().splitlines()]

# Part 1
mapmap: "list[list[int]]" = [[0] * 1000 for x in range(1000)]
for vector in vectors:
    mapmap = vector.overdrawMatrix(mapmap, False)
print(sum(findOverlap(mapmap)))

# Part 2
mapmap: "list[list[int]]" = [[0] * 1000 for x in range(1000)]
for vector in vectors:
    mapmap = vector.overdrawMatrix(mapmap, True)
print(sum(findOverlap(mapmap)))