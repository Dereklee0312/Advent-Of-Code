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
- Need to represent each shape in a format that will allow movement vertically and horizontally
- Need to keep track of height of highest rock
- Need to rotate through list of rock types and Jet directions
- Need to spawn rock 3 higher (exclusive) from highest rock or bottom of pit
- Keep track of bottom of rock and left side of rock to properly spawn it


- resetting the grid each time rock lands and keep track of height is an option, since the rock always spawns 3 units higher than highest rock or floor
- if rock goes past highest rock, just discard it?
- Actually cannot do that since it will falsify the air jet pattern as we dont know how many iterations it would take for it to land

- Might need to create an object for each shape when spawning it.
- Can then easily modify the coordinates of the shape without having to keep track of individual points in the grid
"""


class Rock:
    def __init__(self, coords: list[tuple[int, int]]):
        self.coords = coords


def spawnRock(iter: int, top: int, grid: list[list[str]]):
    """
    Method to place the shape onto grid; given highest rock is given
    """
    sLst = ["-", "+", "L", "l", "o"]
    shapes = {}
    coords = []

    shapes["-"] = [(-4, 3), (-4, 4), (-4, 5), (-4, 6)]
    shapes["+"] = [(-4, 4), (-5, 3), (-5, 4), (-5, 5), (-6, 4)]
    shapes["L"] = [(-4, 3), (-4, 4), (-4, 5), (-5, 5), (-6, 5)]
    shapes["l"] = [(-4, 3), (-5, 3), (-6, 3), (-7, 3)]
    shapes["o"] = [(-4, 3), (-4, 4), (-5, 3), (-5, 4)]

    cycle = iter % 5
    for row, col in shapes[sLst[cycle]]:
        coords.append((top + row, col))
        # grid[top + row][col] = "@"

    newRock = Rock(coords)

    return newRock


def moveHorizontal(dir: str, rock: Rock, grid: list[list[str]]):
    right = 1
    left = -1
    newPos = []
    forbidden = ["|", "-", "#"]
    for row, col in rock.coords:
        if dir == ">":
            newCol = col + right
        else:
            newCol = col + left
        newPos.append((row, newCol))

    for row, col in newPos:
        if grid[row][col] in forbidden:
            return rock

    return Rock(newPos)


def moveVertical(rock: Rock, grid: list[list[str]]):
    newPos = []
    forbidden = ["|", "-", "#"]

    for row, col in rock.coords:
        newRow = row + 1
        newPos.append((newRow, col))

    for row, col in newPos:
        if grid[row][col] in forbidden:
            return rock

    return Rock(newPos)


def main():
    # grid = [["." for _ in range(9)] for _ in range(2023 * 4 + 1)]
    grid = [["." for _ in range(9)] for _ in range(10)]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (j == 0 or j == len(grid[0]) - 1) and i != len(grid) - 1:
                grid[i][j] = "|"
            if i == len(grid) - 1 and (j == 0 or j == len(grid[0]) - 1):
                grid[i][j] = "+"
            elif i == len(grid) - 1:
                grid[i][j] = "-"

    rock = spawnRock(4, len(grid) - 1, grid)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end="")
        print()

    for i, j in rock.coords:
        print(i, j)


if __name__ == "__main__":
    main()
