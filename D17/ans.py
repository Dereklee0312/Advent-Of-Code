#!/usr/bin/python3

from helper import *

lines = parseFile()

direction = []

for dir in lines[0]:
    direction.append(dir)

dirMod = len(direction)

# Assigning points for the shape where it will spawn.
# Spawning shapes will always be in same position
# Row = 0 Since verticality is dependent on highest rock

grid = [["." for _ in range(9)] for _ in range(2022 * 4 + 1)]
# # grid = [["." for _ in range(9)] for _ in range (30)]

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (j == 0 or j == len(grid[0]) - 1) and i != len(grid) - 1:
            grid[i][j] = "|"
        if i == len(grid) - 1 and (j == 0 or j == len(grid[0]) - 1):
            grid[i][j] = "+"
        elif i == len(grid) - 1:
            grid[i][j] = "-"


# print(direction[78 % 40])

top = len(grid) - 1

dirCount = 0
for i in range(2022):
    cont = True

    rock = spawnRock(i, top, grid)
    while cont:
        curDir = direction[dirCount % dirMod]
        # print(curDir)
        rock, cont = moveHorizontal(curDir, rock, grid)

        if cont == True:
            rock,cont = moveVertical(rock, grid)

        dirCount += 1

    top = findHighest(grid)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        print(grid[i][j], end="")
    print()

print(len(grid) - 1 - findHighest(grid))
