def genList(fileName):
    numList = [[], [], [], [], [], [], [], [], []]
    count = 1
    skip = [" ", "[", "]", "\n"]
    with open(fileName) as f:
        for line in f:
            if count <= 8:
            # if count <= 3:
                for i, a in enumerate(line):
                    if a not in skip:
                        index = int(i/4 - 0.25)
                        numList[index].insert(0, a)
            count += 1
    return numList

def moveCrate1(_num, _from, _to, _lst):
    for i in range(_num):
        _lst[_to - 1].append(_lst[_from - 1].pop())

    return _lst

def moveCrate2(_num, _from, _to, _lst):
    newLst = []
    for i in range(_num):
        newLst.append(_lst[_from - 1].pop())
    for i in range(_num):
        _lst[_to - 1].append(newLst.pop())

    return _lst


if __name__ == "__main__":
    lst = genList("test.txt")

    with open("test.txt") as f:
        for line in f:
            if line.startswith("m"):
                num = [int(s) for s in line.split() if s.isdigit()]
                # lst = moveCrate1(num[0], num[1], num[2], lst)
                lst = moveCrate2(num[0], num[1], num[2], lst)

    string = ""
    for i in lst:
        string += i.pop()

    print(string)
