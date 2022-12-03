# Advent Of Code
# Author: Derek Lee
# Language: Python
# Day: 2

# Part 1
class RPS1:
    def __init__(self):
        self.totalPoints = 0
        self.pts = {"X" : 1, "Y" : 2, "Z" : 3}

    def gameplay(self, p1, p2):
        if p2 == "X":
            if p1 == "B":
                self.totalPoints += self.pts[p2]
            elif p1 == "C":
                self.totalPoints += self.pts[p2] + 6
            else:
                self.totalPoints += self.pts[p2] + 3
        elif p2 == "Y":
            if p1 == "A":
                self.totalPoints += self.pts[p2] + 6
            elif p1 == "C":
                self.totalPoints += self.pts[p2]
            else:
                self.totalPoints += self.pts[p2] + 3
        elif p2 == "Z":
            if p1 == "A":
                self.totalPoints += self.pts[p2]
            elif p1 == "B":
                self.totalPoints += self.pts[p2] + 6
            else:
                self.totalPoints += self.pts[p2] + 3


# Part 2
class RPS2:
    def __init__(self):
        self.totalPoints = 0
        self.pts = {"X": 0, "Y": 3, "Z": 6}
        self.handPts = {"A": 1, "B": 2, "C": 3}

    def gameplay(self, p1, p2):
        if p2 == "X":
            if p1 == "B":
                self.totalPoints += self.handPts["A"]
            elif p1 == "C":
                self.totalPoints += self.handPts["B"]
            else:
                self.totalPoints += self.handPts["C"]
        elif p2 == "Y":
            self.totalPoints += self.handPts[p1]
        elif p2 == "Z":
            if p1 == "A":
                self.totalPoints += self.handPts["B"]
            elif p1 == "B":
                self.totalPoints += self.handPts["C"]
            else:
                self.totalPoints += self.handPts["A"]

        self.totalPoints += self.pts[p2]

gameObj = RPS1()
gameObj2 = RPS2()
with open("test.txt") as f:
    for line in f:
        inp = line.split()
        gameObj.gameplay(inp[0], inp[1])
        gameObj2.gameplay(inp[0], inp[1])

print(gameObj.totalPoints)
print(gameObj2.totalPoints)
