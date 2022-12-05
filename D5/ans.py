# numList = [[], [], [], [], [], [], [], [], []]
# count = 1
# skip = [" ", "[", "]", "\n"]
# with open("test.txt") as f:
#     for line in f:
#         if count <= 8:
#             for i, a in enumerate(line):
#                 if a not in skip:
#                     # print(a, i / 4 + 0.75)
#                     index = int(i/4 - 0.25)
#                     numList[index].insert(0, a)
#         count += 1

def genList(fileName):
    numList = [[], [], [], [], [], [], [], [], []]
    count = 1
    skip = [" ", "[", "]", "\n"]
    with open(fileName) as f:
        for line in f:
            if count <= 8:
                for i, a in enumerate(line):
                    if a not in skip:
                        index = int(i/4 - 0.25)
                        numList[index].insert(0, a)
            count += 1
    return numList

def moveCrate(num, from, to):


lst = genList("test.txt")
for i in lst:
    print(i)
