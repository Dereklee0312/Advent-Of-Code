#!/usr/bin/python3

from helper import *

lines = parseFile()

pts = []

facing = {"E": 0, "S": 1, "W": 2, "N": 3}

for row, line in enumerate(lines[:-2]):
    for col, char in enumerate(line):
        if char != " ":
            pts.append((row+1, col+1, char))

num = ""
moveLst = []
for char in lines[-1]:
    if char == "R" or char == "L":
        moveLst.append(int(num))
        moveLst.append(char)
        num = ""
    else:
        num += char
else:
    if num != "":
        moveLst.append(int(num))

dir = "E"
curPos = [pts[0][0], pts[0][1]]

for i in moveLst:
    if type(i) == int:
        curPos = move(curPos, dir, i, pts)
    else:
        dir = rotate(dir, i)

print(1000 * curPos[0] + 4 * curPos[1] + facing[dir])
