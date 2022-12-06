def checkDiff(lst):
    return len(lst) == len(set(lst))

def countCharacters(line):
    charLst = []
    checkLst = []

    for char in line:
        charLst.append(char)

        # if len(checkLst) != 4: # P1
        if len(checkLst) != 14: # P2
            checkLst.append(char)

        else:
            if checkDiff(checkLst):
                return len(charLst) - 1
            else:
                checkLst.pop(0)
                checkLst.append(char)

with open("test.txt") as f:
    for line in f:
        print(countCharacters(line))
