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


def compareLines(lst1, lst2):
    while lst1 and lst2:
        left = lst1.pop(0)
        right = lst2.pop(0)
        print(left)
        print(right, "\n")

        if type(left) == type(right) == int:
            if left > right:
                return -1
            elif left == right:
                continue
            else:
                return 1
        elif type(left) == list and type(right) == int:
            right = [right]
            comparison = compareLst(left, right)
            if comparison == 0:
                continue
            else:
                return comparison

        elif type(left) == int and type(right) == list:
            left = [left]
            comparison = compareLst(left, right)
            if comparison == 0:
                continue
            else:
                return comparison

        else:
            comparison = compareLst(left, right)
            if comparison == 0:
                continue
            else:
                return comparison

    if len(lst1) < len(lst2):
        return 1
    else:
        return -1

def compareLst(lst1, lst2):
    for i in range(len(lst1)):
        left = lst1[i]
        try:
            right = lst2[i]
            if left == right:
                continue
            elif left < right:
                return 1
            else:
                return -1
        except:
            return -1

    if len(lst1) < len(lst2):
        return 1
    return 0

# lst = eval("[1,[2,[3,[4,[5,6,0]]]],8,9]")
# print(type(lst[0]))
