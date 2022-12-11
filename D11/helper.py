import sys
import math


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


class MonkeyLst:
    def __init__(self):
        self.monks = []

    def addMonk(self, monkObj):
        self.monks.append(monkObj)

    def getMonk(self, index):
        for i in self.monks:
            if i.index == index:
                return i

    def playRound(self):
        for monkeys in self.monks:
            for i in range(len(monkeys.items)):
                target, lvl = monkeys.playTurn()
                if target != None:
                    targetMonk = self.getMonk(target)
                    targetMonk.items.append(lvl)



class Monkey:
    def __init__(self, index, items, operation, divider, tMonk, fMonk):
        self.index = index
        self.items = items
        self.operation = operation
        self.divider = divider
        self.tMonk = tMonk
        self.fMonk = fMonk
        self.turns = 0

    def checkTest(self, lvl):
        if lvl % self.divider == 0:
            return True
        return False

    def afterInspect(self, item):
        if "+" in self.operation:
            op = "+"
        else:
            op = "*"

        if self.operation.split()[-1].isdigit():
            if op == "+":
                num = int(self.operation.split("+")[1])
            else:
                num = int(self.operation.split("*")[1])
        else:
            num = item

        if op == "+":
            newLvl = item + num
        else:
            newLvl = item * num

        return math.floor(newLvl/3)

    def playTurn(self):
        if len(self.items) == 0:
            return None, None
        else:
            self.turns += 1
            item = self.items.pop(0)
            lvl = self.afterInspect(item)

            if self.checkTest(lvl):
                monk = self.tMonk
            else:
                monk = self.fMonk

        return monk, lvl
