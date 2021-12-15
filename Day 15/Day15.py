
from collections import defaultdict
import heapq
import timeit

with open("Day 15/Day15", "r") as file:
    data = [[int(item) for item in list(line)] for line in file.read().splitlines()]

# Expand Data 5x


#Expand Y Ways
yPanded = [[(i+y-1)%9 +1 for i in line] for y in range(5) for line in data]
#Expand X Ways
xPanded = [[(i+x-1)%9 +1 for x in range(5) for i in line] for line in yPanded]
bigData = xPanded



position = tuple[int, int]

def search(map, start: position, end: position, h):

    xCoord = len(map) - 1
    yCoord = len(map[0]) - 1

    def getCost(pos: position):
        return map[pos[0]][pos[1]]

    def getNeighbours(pos: position):
        x, y = pos
        out: list[position] = []
        if x > 0: out.append((x-1, y))
        if x < xCoord: out.append((x+1, y))
        if y > 0: out.append((x, y-1))
        if y < yCoord: out.append((x, y+1))
        return out

    def unravel(cameFrom: dict, current: position):
        completePath = [getCost(current)]
        while current in cameFrom.keys():
            current = cameFrom[current]
            completePath.append(getCost(current))
        return list(reversed(completePath[:-1]))

    bestPaths = {}

    knownScore = defaultdict(lambda: pow(2, 32))
    knownScore[start] = 0

    searchingNodes = [(h(start), start)]

    while searchingNodes:
        # Peek smallest node
        # This should always exist as long as
        #   SearchingNodes has an item
        if searchingNodes[0][1] == end:
            return unravel(bestPaths, end);

        _, currentNode = heapq.heappop(searchingNodes)

        for neighbour in getNeighbours(currentNode):
            costThisPath = knownScore[currentNode] + getCost(neighbour)
            if costThisPath < knownScore[neighbour]:
                # This path is better, update
                knownScore[neighbour] = costThisPath
                estimatedScore = costThisPath + h(neighbour)
                bestPaths[neighbour] = currentNode

                if neighbour not in [node for _, node in searchingNodes]:
                    heapq.heappush(searchingNodes, (estimatedScore, neighbour))

    return []

        


def manhattenToEnd(pos: position, end: position):
    return (end[0] - pos[0]) + (end[1] - pos[1])

def negativeScore(pos: position):
    return (-pos[0]) + (-pos[1])

def zero(pos: position):
    return 0
    
def findTopLeftToBottomRight(data):
    xCoord = len(data) - 1
    yCoord = len(data[0]) - 1
    return search(data, (0,0), (xCoord, yCoord), negativeScore)

if __name__ == '__main__':

    
    print(sum(findTopLeftToBottomRight(data)))
    print(sum(findTopLeftToBottomRight(bigData)))

    print("Done")