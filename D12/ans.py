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

print(move(grid, sRow, sCol, maxRow, maxCol))
