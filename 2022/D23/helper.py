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


"""
Remember to consider empty soil outside of point list, need to expand the map dynamically

Keep track of which elf's proposed movement
LST = [Identifier, proposed location]

Go through the list and pop it while checking if popped item is in list.
- If in list, pop that item as well and add those identifiers to a list

Check which proposed movement intersect

NOTE: MORE THAN TWO ELVES MAY PROPOSE THE SAME LOCATION
"""


def updateElves(elves, round):
    """
    Function to generate a list of proposal positions for elves
    """
    newPos = {}
    dups = []
    checkElves = elves.copy()

    for id, (row, col) in elves.items():
        newRow, newCol = findNextPos(row, col, elves, round)
        # newPos[id] = [newRow, newCol]

        if [newRow, newCol] not in newPos.values() and [newRow, newCol] not in dups:
            newPos[id] = [newRow, newCol]
        else:
            for i, (row, col) in newPos.items():
                if newRow == row and newCol == col:
                    break
            newPos.pop(i)
            dups.append([newRow, newCol])

    for i, (row, col) in newPos.items():
        elves[i] = [row, col]

    if elves == checkElves:
        return elves, False
    else:
        return elves, True


def findNextPos(curRow, curCol, pts, round):
    """
    Generates a list of [ID, NEXT_ROW, NEXT_COL]
    """
    dir = {
        "N": [-1, 0],
        "NE": [-1, 1],
        "NW": [-1, -1],
        "S": [1, 0],
        "SE": [1, 1],
        "SW": [1, -1],
        "E": [0, 1],
        "W": [0, -1],
    }
    north = {
        "N": [-1, 0],
        "NE": [-1, 1],
        "NW": [-1, -1],
    }
    south = {
        "S": [1, 0],
        "SE": [1, 1],
        "SW": [1, -1],
    }
    west = {
        "W": [0, -1],
        "NW": [-1, -1],
        "SW": [1, -1],
    }
    east = {
        "E": [0, 1],
        "NE": [-1, 1],
        "SE": [1, 1],
    }

    propChecks = [north, south, west, east]

    for i in range(round):
        propChecks.append(propChecks.pop(0))

    for i, j in dir.values():
        newRow = curRow + i
        newCol = curCol + j

        if [newRow, newCol] in pts.values():
            break
    else:
        return [curRow, curCol]

    for props in propChecks:
        for i, j in props.values():
            newRow = curRow + i
            newCol = curCol + j

            if [newRow, newCol] in pts.values():
                break
        else:
            if props == north:
                return [curRow + dir["N"][0], curCol + dir["N"][1]]

            elif props == south:
                return [curRow + dir["S"][0], curCol + dir["S"][1]]

            elif props == west:
                return [curRow + dir["W"][0], curCol + dir["W"][1]]

            else:
                return [curRow + dir["E"][0], curCol + dir["E"][1]]
    return [curRow, curCol]


def findBoundaries(elves):
    row = []
    col = []
    for i, j in elves.values():
        row.append(i)
        col.append(j)

    return min(row), min(col), max(row), max(col)
