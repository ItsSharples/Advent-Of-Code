from math import gcd


def toLocations(line) -> list:
    # Convert 'x1,y1 -> x2,y2' to x1, y1, x2, y2
    (x1,y1), (x2,y2) = (map(int, pair) for pair in (point.split(',') for point in line.split(" -> ")))
    (minX, maxX) = (x1, x2) if x1 < x2 else (x2, x1)
    (minY, maxY) = (y1, y2) if y1 < y2 else (y2, y1)
    diagonal = (x2 - x1, y2 - y1)
    divisor = abs(gcd(*diagonal))
    lerp = lambda a, b, t : list(a[i] + b[i] * t for i in range(2))
    step = list(int(int(diagonal[i])/divisor) for i in range(2))

    return [ [x1, y] for y in range(minY, maxY + 1)] if x1 == x2 \
      else [ [x, y1] for x in range(minX, maxX + 1)] if y1 == y2 \
      else [ lerp((x1, y1), step, d) for d in range(divisor + 1)]

with open("Day 5/Day5", "r") as file:
    vectors = [toLocations(line) for line in file.read().splitlines()]

mapmap = [[0] * 1000 for x in range(1000)]
for locations in vectors:
    for location in locations:
        mapmap[location[0]][location[1]] += 1

out = sum([1 if x > 1 else 0 for y in mapmap for x in y ])
print(out)