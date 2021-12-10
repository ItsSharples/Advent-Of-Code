from collections import Counter
from functools import reduce

import numpy as np
import matplotlib.pyplot as plt

data: list[list[int]]
with open("Day 9/Day9", "r") as dataFile:
    data = np.array([[int(item) for item in line] for line in dataFile.read().splitlines()])

output = np.array(data, dtype=int, copy=True)
minCoords = list()
for passOver in range(9):
    for x, line in enumerate(output):
        for y, item in enumerate(line): 
            left, right, top, bottom = 9,9,9,9

            if x > 0: left = output[x-1][y]
            if x < 99: right = output[x+1][y]
            if y > 0: top = output[x][y-1]
            if y < 99: bottom = output[x][y+1]

            #First Pass, find lowest point, these are markers
            if passOver == 0:
                if min(left, right, top, bottom, item) == item:
                    minCoords.append((x,y))
                    item = -len(minCoords)

            # output[x][y] = ((x,y),left, right, top, bottom, item, (data[x-1][y]))
            if item == 9: output[x][y] = 9
            else: output[x][y] = min(left, right, top, bottom, item)

counter = Counter(output.flat)
commonBasins = counter.most_common(4)[1:]
sum = reduce(lambda current, pair: current * pair[1], commonBasins, 1)
print(sum)


plt.figure()
plt.imshow(output, cmap='ocean')
plt.show()