#!/usr/bin/python3

from helper import *

lines = parseFile()

coords = []
collide = 0

for line in lines:
    x, y, z = line.split(",")
    x, y, z = int(x), int(y), int(z)
    coords.append((x, y, z))

    for X, Y, Z in coords[:-1]:
        if (
            (abs(X - x) == 1 and Y == y and Z == z)
            or (X == x and abs(Y - y) == 1 and Z == z)
            or (X == x and Y == y and abs(Z - z) == 1)
        ):
            collide += 1

print(len(coords) * 6 - collide * 2)
