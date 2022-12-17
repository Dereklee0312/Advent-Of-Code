#!/usr/bin/python3

from helper import *

lines = parseFile()

direction = []

shapes = {}

# Assigning points for the shape where it will spawn.
# Spawning shapes will always be in same position
# Row = 0 Since verticality is dependent on highest rock
sLst = ["-", "+", "L", "l", "o"]

shapes["-"] = [(0, 3), (0, 4), (0, 5), (0, 6)]
shapes["+"] = [(0, 4), (-1, 3), (-1, 4), (-1, 5), (-2, 4)]
shapes["L"] = [(0, 3), (0, 4), (0, 5), (-1, 5), (-2, 5)]
shapes["l"] = [(0, 3), (-1, 3), (-2, 3), (-3, 3)]
shapes["o"] = [(0, 3), (0, 4), (-1, 3), (-1, 3)]

for dir in lines[0]:
    direction.append(dir)

grid = [["." for _ in range(9)] for _ in range(2023 * 4 + 1)]
# grid = [["." for _ in range(9)] for _ in range (30)]

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (j == 0 or j == len(grid[0]) - 1) and i != len(grid) - 1:
            grid[i][j] = "|"
        if i == len(grid) - 1 and (j == 0 or j == len(grid[0]) - 1):
            grid[i][j] = "+"
        elif i == len(grid) - 1:
            grid[i][j] = "-"

for i in range(len(grid)):
    for j in range(len(grid[0])):
        print(grid[i][j], end="")
    print()

print(len(grid))
