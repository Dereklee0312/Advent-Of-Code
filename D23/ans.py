#!/usr/bin/python3

from helper import *

lines = parseFile()

"""
KEY: Elf identifier
VALUES: ROW, COL
"""
elves = {}

elfNum = 0

for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char == "#":
            elves[elfNum] = [row, col]
            elfNum += 1

for i in range(10):
    elves = updateElves(elves, i)

count = 0
mRow, mCol, MRow, MCol = findBoundaries(elves)

for i in range(mRow, MRow + 1):
    for j in range(mCol, MCol + 1):
        if [i, j] not in elves.values():
            count += 1

print(count)
