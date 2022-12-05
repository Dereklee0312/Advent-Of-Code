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

def moveCrate(_num, _from, _to, _lst):
    for i in range(_num):
        _lst[_to - 1].append(_lst[_from - 1].pop())

    return _lst

lst = genList("test.txt")

with open("test.txt") as f:
    for line in f:
        if line.startswith("m"):
            num = [int(s) for s in line.split() if s.isdigit()]
            lst = moveCrate(num[0], num[1], num[2], lst)

string = ""
for i in lst:
    string += i.pop()

print(string)
