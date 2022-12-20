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


def whatNum(lst, cur, after):
    index = cur + after
    while index > len(lst) - 1:
        index -= len(lst)

    return index
