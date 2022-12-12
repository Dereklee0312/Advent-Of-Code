#!/usr/bin/python3

from helper import *

sRow, sCol, maxRow, maxCol, lines = parseFile()

dict = createDict()

dict["S"] = 1
dict["E"] = 26
grid = []

for i, line in enumerate(lines):
    lst = []
    for j, a in enumerate(line):
        point = Point(a, dict[a], i, j)
        lst.append(point)
    grid.append(lst)

posLocations = []

for i in range(maxRow):
    for j in range(maxCol):
        if grid[i][j].char == "a" or grid[i][j].char == "S":
            count = move(grid, i, j, maxRow, maxCol)
            if count != None:
                posLocations.append(count)
            resetGrid(grid, maxRow, maxCol)

print("Part 1: ", move(grid, sRow, sCol, maxRow, maxCol))
print("Part 2: ", min(posLocations))
