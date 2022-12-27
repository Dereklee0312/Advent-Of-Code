import sys


def parseFile():
    if len(sys.argv) == 1:
        filename = "demo.txt"
    else:
        filename = "input.txt"

    lines = []
    with open(filename) as f:
        for line in f:
            lines.append(line.rstrip())

    return lines


def move(curPos, dir, amt, pts):
    map = {"E": (0, 1), "S": (1, 0), "W": (0, -1), "N": (-1, 0)}

    for _ in range(amt):
        nextRow = curPos[0] + map[dir][0]
        nextCol = curPos[1] + map[dir][1]

        if (nextRow, nextCol, "#") in pts:
            return curPos
        elif (nextRow, nextCol, ".") in pts:
            curPos[0] = nextRow
            curPos[1] = nextCol
        else:
            nextRow, nextCol = getWrap(curPos, dir, pts)
            if (nextRow, nextCol, "#") in pts:
                return curPos
            else:
                curPos[0] = nextRow
                curPos[1] = nextCol

    return curPos


def rotate(curDir, dir):
    cardinals = ["E", "S", "W", "N"]
    map = {"E": 0, "S": 1, "W": 2, "N": 3}

    if dir == "R":
        index = (map[curDir] + 1) % len(cardinals)

    else:
        index = (map[curDir] - 1) % len(cardinals)

    return cardinals[index]


def getWrap(curPos, dir, pts):
    if dir == "E" or dir == "W":
        cols = []
        for (i, j, _) in pts:
            if i == curPos[0]:
                cols.append(j)
        return (curPos[0], min(cols)) if dir == "E" else (curPos[0], max(cols))

    else:
        rows = []
        for (i, j, _) in pts:
            if j == curPos[1]:
                rows.append(i)
        return (min(rows), curPos[1]) if dir == "S" else (max(rows), curPos[1])
