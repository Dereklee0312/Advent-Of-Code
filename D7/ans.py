class Directory:
    def __init__(self, name):
        self.name = name
        self.totalData = 0
        self.childDir = []

    def addData(self, data):
        self.totalData += data

    def addChild(self, child):
        self.childDir.append(child)

    # def getChildTotal(self):
    #     total = 0
    #     for i in self.childDir:
    #         total += i.getTotal()

    def getTotal(self):
        return self.totalData


def findDir(lst, dirName):
    for i in lst:
        if i.name == dirName:
            return i
"""
Gonna use recursion with a queue mayB to do DFS and calculate total size of each nested directory.

Find size of each directory, then check if <= 100,000

When 'cd ..' should add size of child dir to parent dir
"""

# depth = -1
# dirLst = []
# with open("test2.txt") as f:
#     for line in f:
#         cmd = line.strip().split()
#         if cmd[1] == "cd" and cmd[2] != "..":
#             newDir = Directory(cmd[2])
#             dirLst.append(newDir)
#             depth += 1
#         elif cmd[1] == "cd" and cmd[2] == "..":
#             dirLst[depth - 1].addData(dirLst[depth].getTotal())
#             depth -= 1
#         if cmd[0].isdigit():
#             dirLst[depth].addData(int(cmd[0]))
