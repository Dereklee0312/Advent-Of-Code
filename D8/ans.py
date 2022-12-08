# PART 1
grid = []
file = "input.txt"

with open(file) as f:
    for line in f:
        arr = [int(x) for x in line if x != "\n"]
        grid.append(arr)

"""
Gotta check until the edge -.-
"""


def checkRow(grid, lst, row, col):
    rowLst = [grid[row][i] for i in lst]
    if grid[row][col] > max(rowLst):
        return True


def checkCol(grid, lst, row, col):
    colLst = [grid[i][col] for i in lst]
    if grid[row][col] > max(colLst):
        return True


def checkSurround(grid, row, col):
    top = [x for x in range(row - 1, -1, -1)]
    bot = [x for x in range(row + 1, len(grid))]
    left = [x for x in range(col - 1, -1, -1)]
    right = [x for x in range(col + 1, len(grid))]

    if (
        checkRow(grid, left, row, col)
        or checkRow(grid, right, row, col)
        or checkCol(grid, top, row, col)
        or checkCol(grid, bot, row, col)
    ):
        return True


skip = [0, len(grid) - 1]
count = 0
for i in range(len(grid)):
    for j in range(len(grid)):
        if i not in skip and j not in skip:
            if checkSurround(grid, i, j):
                count += 1
        else:
            count += 1

print(count)
