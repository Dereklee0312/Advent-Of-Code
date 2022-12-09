class Dir:
    def __init__(self, name):
        self.name = name
        self.totalData = 0
        self.childDir = []
        self.numChild = 0

    def addData(self, name, data):
        curDir = self.findDir(name)
        if curDir != None:
            curDir.totalData += data
        else:
            self.totalData += data

        # if name == "e":
        #     print(curDir, "addDATA")

    def getTotal(self):
        return self.totalData

    def findDir(self, name):
        for i in self.childDir:
            # if name == "e":
            #     print(i.name, "findDIR")
            if i.name == name:
                return i
            else:
                i.findDir(name)

        return None

    def addChild(self, parent, childObj):
        parentDir = self.findDir(parent)
        if parentDir != None:
            parentDir.childDir.append(childObj)

        else:
            self.childDir.append(childObj)

    def dispChild(self):
        for i in self.childDir:
            i.dispChild()
            print(i.name, i.totalData)


parentDir = ["/"]
home = Dir("/")
curDir = "/"
with open("test2.txt") as f:
    for index, line in enumerate(f):
        if index > 0:
            cmd = line.strip().split()

            if cmd[1] == "cd" and cmd[2] != "..":
                curDir = cmd[2]
                parentDir.append(cmd[2])
                childDir = Dir(cmd[2])
                print(index, parentDir[-2], cmd[2])
                home.addChild(parentDir[-2], childDir)

            elif cmd[1] == "cd" and cmd[2] == "..":
                curDir = parentDir.pop()

            elif cmd[0].isdigit():
                # print(curDir, cmd[0])
                home.addData(curDir, int(cmd[0]))


# print(parentDir)
# home.dispChild()
