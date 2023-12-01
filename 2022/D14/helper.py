import sys


def parseFile():
    if len(sys.argv) == 1:
        filename = "demo.txt"
    else:
        filename = "input.txt"

    lines = []
    with open(filename) as f:
        for line in f:
            lines.append(line.strip())

    return lines


def moveSand(sRow, sCol, grid, MRow):
    """
    Part 1
    Function to move a grain of salt until it reaches a stable position
    1 - Check if nextRow is a valid position or else it counts as falling in abyss and thus breaks out function
    2 - If nextPos (vertically down) is not a rock or sand, assign nextPos as currentPos and continue
    3 - If nextPos (vertically down) is a rock or sand, check diagonally to left for same conditions
    4 - If Pos is rock or sand, check diagonally to right for same conditions
    5 - If all above conditions are not met, sand settles
    """
    cont = True
    curRow = sRow
    curCol = sCol
    down = (1, 0)
    SW = (1, -1)
    SE = (1, 1)
    restPts = ["o", "#"]
    while cont:
        nextRow = curRow + down[0]
        nextCol = curCol + down[1]
        if nextRow <= MRow:
            if grid[nextRow][nextCol] not in restPts:
                curRow = nextRow
                curCol = nextCol
                continue
            else:
                nextRow = curRow + SW[0]
                nextCol = curCol + SW[1]

                if grid[nextRow][nextCol] not in restPts:
                    curRow = nextRow
                    curCol = nextCol
                    continue
                else:
                    nextRow = curRow + SE[0]
                    nextCol = curCol + SE[1]
                    if grid[nextRow][nextCol] not in restPts:
                        curRow = nextRow
                        curCol = nextCol
                        continue
                    else:
                        grid[curRow][curCol] = "o"
                        break
        else:
            return -1

def moveSand2(sRow, sCol, grid, MRow, MCol):
    """
    Part 2:
    Logic same as Part 1
    Added MCol and used try/except since not all rows/cols are in grid
    """
    cont = True
    curRow = sRow
    curCol = sCol
    down = (1, 0)
    SW = (1, -1)
    SE = (1, 1)
    restPts = ["o", "#"]
    while cont:
        nextRow = curRow + down[0]
        nextCol = curCol + down[1]
        if nextRow <= MRow and nextCol <= MCol:
            try:
                if grid[nextRow][nextCol] not in restPts:
                    curRow = nextRow
                    curCol = nextCol
                    continue
                else:
                    nextRow = curRow + SW[0]
                    nextCol = curCol + SW[1]

                    if grid[nextRow][nextCol] not in restPts:
                        curRow = nextRow
                        curCol = nextCol
                        continue
                    else:
                        nextRow = curRow + SE[0]
                        nextCol = curCol + SE[1]
                        if grid[nextRow][nextCol] not in restPts:
                            curRow = nextRow
                            curCol = nextCol
                            continue
                        else:
                            grid[curRow][curCol] = "o"
                            break
            except:
                break
        else:
            return -1
