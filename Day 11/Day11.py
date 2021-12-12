
from collections import defaultdict

with open("Day 11/Small", "r") as file:
    pairs = [tuple(line.split("-")) for line in file.read().splitlines()]

nodes = defaultdict(list[str])
for (start, end) in pairs:
    nodes[start].append(end)
    nodes[end].append(start)

def search(currentPath = ["start"], cannotTraverse: list[str] = ["start"], exploredSmall = "") -> list[list[str]]:
    out = []
    for newNode in nodes[currentPath[-1]]:
        newPath = currentPath + [newNode]
        if newNode == "start": continue
        if newNode == "end": out.__iadd__([newPath]); continue

        exploredSmallYet = exploredSmall
        if newNode in cannotTraverse:
            if not exploredSmallYet: exploredSmallYet = newNode
            if exploredSmallYet != newNode: continue
            if cannotTraverse.count(newNode) > 1: continue

        out.__iadd__(search(newPath, cannotTraverse.__add__([newNode] if newNode.islower() else []), exploredSmallYet))
    return out


part1 = search(exploredSmall="WamIsAMassiveCutie");
part2 = search();
print(len(part1), len(part2))
