# PART 2
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
    count = 0
    rowLst = [grid[row][i] for i in lst]
    for i in rowLst:
        if grid[row][col] > i:
            count += 1
        else:
            count += 1
            return count

    return count


def checkCol(grid, lst, row, col):
    count = 0
    colLst = [grid[i][col] for i in lst]
    for i in colLst:
        if grid[row][col] > i:
            count += 1
        else:
            count += 1
            return count

    return count


def checkSurround(grid, row, col):
    countLst = []
    product = 1
    top = [x for x in range(row - 1, -1, -1)]
    bot = [x for x in range(row + 1, len(grid))]
    left = [x for x in range(col - 1, -1, -1)]
    right = [x for x in range(col + 1, len(grid))]

    countLst.append(checkRow(grid, left, row, col))
    countLst.append(checkRow(grid, right, row, col))
    countLst.append(checkCol(grid, top, row, col))
    countLst.append(checkCol(grid, bot, row, col))

    for i in countLst:
        product *= i

    return product


skip = [0, len(grid) - 1]
prodLst = []
for i in range(len(grid)):
    for j in range(len(grid)):
        if i not in skip and j not in skip:
            prodLst.append(checkSurround(grid, i, j))
print(max(prodLst))
