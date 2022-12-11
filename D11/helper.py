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


def multiply(num1, num2):
    return num1 * num2


def add(num1, num2):
    return num1 + num2


class MonkeyLst:
    def __init__(self):
        self.numMonks = 0
        self.monks = {}

    def addMonk(self, monkObj):
        self.monks[self.numMonks] = monkObj
        self.numMonks += 1

    def playRound(self):
        for monkeys in self.monks.values():
            for _ in range(len(monkeys.items)):
                target, lvl = monkeys.playTurn()
                self.monks[target].items.append(lvl)


class Monkey:
    def __init__(self, index, items, operation, divider, tMonk, fMonk):
        self.index = index
        self.items = items
        self.operation = operation
        self.divider = divider
        self.tMonk = tMonk
        self.fMonk = fMonk
        self.turns = 0
        if "+" in self.operation:
            self.op = add
        else:
            self.op = multiply

        if self.operation.split()[-1].isdigit():
            self.num = int(self.operation.split()[-1])
        else:
            self.num = None

    # def afterInspect(self, item):
    #     if self.num == None:
    #         num = item
    #     else:
    #         num = self.num
    #
    #     newLvl = self.op(item, num)
    #
    #     return newLvl
    # return math.floor(newLvl/3)

    def playTurn(self):
        # if len(self.items) == 0:
        #     return None, None
        # else:
        item = self.items.pop(0)
        num = item if self.num == None else self.num

        self.turns += 1
        lvl = self.op(item, num)

        if lvl % self.divider == 0:
            return self.tMonk, lvl
        else:
            return self.fMonk, lvl
