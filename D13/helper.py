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


def compareLst(lst1, lst2):
    if type(lst1) == list and type(lst2) == int:
        lst2 = [lst2]
    if type(lst1) == int and type(lst2) == list:
        lst1 = [lst1]
    if type(lst1) == int and type(lst2) == int:
        if lst1 < lst2:
            return 1
        elif lst1 > lst2:
            return -1
        return 0
    if type(lst1) == list and type(lst2) == list:
        i = 0

        while i < len(lst1) and i < len(lst2):
            cont = compareLst(lst1[i], lst2[i])

            if cont == 1:
                return 1
            elif cont == -1:
                return -1

            i += 1

        if i == len(lst1):
            if len(lst1) == len(lst2):
                return 0
            return 1

        return -1
