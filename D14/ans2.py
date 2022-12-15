#!/usr/bin/python3

from helper import *

lines = parseFile()

coords = []

for cmd in lines:
    cmd = cmd.split("->")
    for xy in cmd:
        coords.append((int(xy.split(",")[0]), int(xy.split(",")[1])))

rows, cols = [y for x, y in coords], [x for x, y in coords]

MRow = max(rows) + 2
mCol = min(cols)
MCol = max(cols) + MRow * 2

grid = [["." for _ in range(MCol - mCol + 1)] for _ in range(MRow + 1)]

deltaRow = MRow + 1
deltaCol = MCol - mCol + 1

for cmd in lines:
    coords = []
    cmd = cmd.split("->")
    for xy in cmd:
        coords.append((int(xy.split(",")[1]), int(xy.split(",")[0])))
    for i, (row, col) in enumerate(coords):
        if i + 1 < len(coords):
            for a in range( x := abs(row - coords[i+1][0]) + 1 if row != coords[i+1][0] else 0):
                if row > coords[i+1][0]:
                    a = -a
                grid[row + a][col - mCol] = "#"

            for b in range( x := abs(col - coords[i+1][1]) + 1 if col != coords[i+1][1] else 0):
                if col > coords[i+1][1]:
                    b = -b
                grid[row][col + b - mCol] = "#"

for i in range(len(grid[0])):
    grid[MRow][i] = "#"

start = True
count = 0
while start:
    count += 1
    cont = moveSand2(0, 500 - mCol, grid, MRow,  500-mCol + 162)
    start = False if grid[0][500-mCol] == "o" else True

# for i in range(deltaRow):
#     for j in range(deltaCol):
#         print(grid[i][j], end="")
#     print()

print(count)
