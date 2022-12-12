import sys


def parseFile():
    if len(sys.argv) == 1:
        filename = "demo.txt"
        maxRow = 5
        maxCol = 8
        sRow, sCol = 0, 0
    else:
        filename = "input.txt"
        maxRow = 41
        maxCol = 162
        sRow, sCol = 20, 0

    lines = []
    with open(filename) as f:
        for line in f:
            lines.append(line.strip())

    return sRow, sCol, maxRow, maxCol, lines


def createDict():
    alpha = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    dict = {}
    for i in range(26):
        dict[alpha[i]] = i + 1

    return dict


class Point:
    def __init__(self, char, value, row, col):
        self.char = char
        self.visited = False
        self.value = value
        self.row = row
        self.col = col


def move(grid, curRow, curCol, maxRow, maxCol):
    movements = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    curPos = grid[curRow][curCol]

    queue = []
    queue.append((curPos, 0))
    curPos.visited = True

    while queue:
        start, count = queue.pop(0)

        for i, j in movements:
            if 0 <= start.row + i < maxRow and 0 <= start.col + j < maxCol:
                next = grid[start.row + i][start.col + j]
                if start.char == "E":
                    return count
                if next.value - start.value <= 1 and next.visited == False:
                    next.visited = True
                    queue.append((next, count + 1))
