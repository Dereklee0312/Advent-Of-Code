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
"""
