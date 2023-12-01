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


def resetLst(lst):
    for i in range(len(lst)):
        lst[i][0] = False

    return lst


def mix(main, copy):
    for i, (_, num) in enumerate(copy):
        index = main.index([i, num])
        removed = main.pop(index)
        to = removed[1]

        if abs(to) >= len(main):
            to %= len(main)

        if 0 < index + to <= len(main) - 1:
            index += to
        elif index + to < 0:
            index += to + len(main)
        elif index + to == 0:
            index = len(main)
        else:
            index += to - len(main)

        main.insert(index, removed)
