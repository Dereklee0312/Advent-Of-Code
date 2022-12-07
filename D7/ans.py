class Directory:
    def __init__(self, name):
        self.name = name
        self.totalData = 0
        self.childDir = []

    def addData(self, data):
        self.totalData += data

    def addChild(self, child):
        self.childDir.append(child)

    def getTotal(self):
        return self.totalData

"""
Gonna use recursion with a queue mayB to do DFS and calculate total size of each nested directory.
"""

totalSize = 0
dirLst = []
with open("test.txt") as f:
    for line in f:
        cmd = line.strip().split()
        if cmd[1] == "cd":
            newDir = Directory(cmd[2])
        elif cmd[1] == "ls":
            if totalSize <= 100000:
                dirLst.append(totalSize)
            totalSize = 0
        elif cmd[0].isdigit():
            totalSize += int(cmd[0])

print(sum(dirLst))
