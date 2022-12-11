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


def updateHead(head, direction):
    motions = {"R": [0, 1], "L": [0, -1], "U": [-1, 0], "D": [1, 0]}
    head[0] += motions[direction][0]
    head[1] += motions[direction][1]


def updateTail(head, tail):
    stat = checkRowCol(head, tail)

    if stat == "Over":
        return
    elif stat == "Row" and (abs(head[1] - tail[1]) == 2):
        if head[1] > tail[1]:
            tail[1] += 1
        else:
            tail[1] -= 1
    elif stat == "Col" and (abs(head[0] - tail[0]) == 2):
        if head[0] > tail[0]:
            tail[0] += 1
        else:
            tail[0] -= 1
    else:
        moveDiagonally(head, tail)


def checkRowCol(head, tail):
    """
    - Check if head and tail are in same column first
    """
    pos = None
    if head[0] == tail[0] and head[1] == tail[1]:
        pos = "Over"  # Overlapping

    elif head[0] == tail[0]:
        pos = "Row"  # Same row

    elif head[1] == tail[1]:
        pos = "Col"  # Same col

    else:
        pos = "Diff"  # Different row and col

    return pos


def moveDiagonally(head, tail):
    """
    - North-East: hrow < trow
                  hcol > tcol

    - North-West: hrow < trow
                  hcol < tcol

    - South-East: hrow > trow
                  hcol > tcol

    - South-West: hrow > trow
                  hcol < tcol
    """
    motions = {"NE": [-1, 1], "NW": [-1, -1], "SE": [1, 1], "SW": [1, -1]}
    targets = [-2, -1, 1, 2]
    absCoords = (
        []
    )  # List of absolute coordinates where target will be according to position of tail
    targetCoords = []
    for i in targets:
        for j in targets:
            if abs(i) != 1 or abs(j) != 1:
                absCoords.append([i, j])
    Trow = tail[0]
    Tcol = tail[1]
    for i in absCoords:
        targetCoords.append([Trow + i[0], Tcol + i[1]])

    if head in targetCoords:
        if head[0] < tail[0]:
            if head[1] > tail[1]:  # North-East
                tail[0] += motions["NE"][0]
                tail[1] += motions["NE"][1]
            else:  # North-West
                tail[0] += motions["NW"][0]
                tail[1] += motions["NW"][1]
        else:
            if head[1] > tail[1]:  # South-East
                tail[0] += motions["SE"][0]
                tail[1] += motions["SE"][1]
            else:  # South-West
                tail[0] += motions["SW"][0]
                tail[1] += motions["SW"][1]


H, T = [0, 0], [0, 0]
k1, k2, k3, k4, k5, k6, k7, k8 = (
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
)

Locations = []

# PART 1
# for motion in lines:
#     direction = motion.split()[0]
#     num = int(motion.split()[1])
#     for i in range(num):
#         updateHead(H, direction)
#         updateTail(H, T)
#         Locations.append(
#             (T[0], T[1])
#         )  # Appending in form of tuples to enable use of set

# PART 2
for motion in lines:
    direction = motion.split()[0]
    num = int(motion.split()[1])
    for i in range(num):
        updateHead(H, direction)
        updateTail(H, k1)
        updateTail(k1, k2)
        updateTail(k2, k3)
        updateTail(k3, k4)
        updateTail(k4, k5)
        updateTail(k5, k6)
        updateTail(k6, k7)
        updateTail(k7, k8)
        updateTail(k8, T)
        Locations.append(
            (T[0], T[1])
        )  # Appending in form of tuples to enable use of set

print(len(set(Locations)))
