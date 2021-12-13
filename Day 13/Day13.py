import numpy
from copy import deepcopy
with open("Day 13/Day13", "r") as file:
    pairs = file.read().split('\n\n')
    data, folds = [[int(item) for item in pair.split(",")] for pair in pairs[0].splitlines()], \
                  [axis.split("=") for axis in [fold.split("fold along ")[1] for fold in pairs[1].splitlines()]]
    
# print(folds)

dataShape = [max([int(datum[0]) for datum in data])+1, max([int(datum[1]) for datum in data])+1]
# print(data)
# print(dataShape)
array = numpy.array([[[x, y] in data for y in range(dataShape[1])] for x in range(dataShape[0])])

for currentFold in folds:
    newShape = deepcopy(list(array.shape))
    if currentFold[0] == 'x':
        axis = 0
        dims = int(currentFold[1])
        split = int(currentFold[1]) * 2 + 1
        newShape[0] = split
    else:
        axis = 1
        dims = int(currentFold[1])
        split = int(currentFold[1]) * 2 + 1
        newShape[1] = split
    
    array.reshape(newShape)

    if currentFold[0] == 'x':
        splitArrays = array[:dims,:], array[dims+1:,:]
    else:
        splitArrays = array[:,:dims], array[:,dims+1:]

    array = splitArrays[0] + numpy.flip(splitArrays[1], axis=axis)

print('\n'.join([''.join(["█" if item else " " for item in line]) for line in array.transpose()]))