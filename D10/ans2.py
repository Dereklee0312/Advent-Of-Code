#!/usr/bin/python3
import sys

if len(sys.argv) == 1:
    filename = "demo.txt"
else:
    filename = "input.txt"

lines = []
with open(filename) as f:
    for line in f:
        lines.append(line.strip())

def draw(grid, cycle, x):
    xLst = [x, x - 1, x + 1]
    if (cycle%40) in xLst:
        grid[cycle//40][cycle%40] = "#"

grid = []
for _ in range(6):
    grid.append([" " for _ in range(40)])


Xval = 1
cycle = 0
signals = {"noop": 1, "addx": 2}

for cmd in lines:
    signal = cmd.split()[0]
    for _ in range(signals[signal]):
        draw(grid, cycle, Xval)
        cycle += 1

    if len(cmd.split()) == 2:
        value = int(cmd.split()[1])
        Xval += value

for i in range(6):
    for j in range(40):
        print(grid[i][j], end="")
    print("")
