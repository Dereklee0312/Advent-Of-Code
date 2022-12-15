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
