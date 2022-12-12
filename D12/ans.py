#!/usr/bin/python3

from helper import *

lines = parseFile()

dict = createDict()

dict["S"] = 1
dict["E"] = 26
grid = []

for i, line in enumerate(lines):
    lst = []
    for j, a in enumerate(line):
        point = Point(a, dict[a], i, j)
        lst.append(point)
        if a == "S":
            sRow = i
            sCol = j
        elif a == "E":
            eRow = i
            eCol = j
    grid.append(lst)

maxRow = len(grid)
maxCol = len(grid[0])

posLocations = []

print("Part 1: ", move(grid, sRow, sCol, maxRow, maxCol))
resetGrid(grid, maxRow, maxCol)
print("Part 2: ", move2(grid, eRow, eCol, maxRow, maxCol))
