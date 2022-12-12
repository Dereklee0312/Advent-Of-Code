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


def multiply(num1, num2, divider):
    # if num1 % divider == 0 or num2 % divider == 0:
    #     return divider
    return num1 * num2


def add(num1, num2, divider):
    # if (num1 + num2) % divider == 0:
    #     return divider
    return num1 + num2


class MonkeyLst:
    def __init__(self):
        self.numMonks = 0
        self.monks = {}

    def addMonk(self, monkObj):
        self.monks[self.numMonks] = monkObj
        self.numMonks += 1

    def playRound(self, part):
        for monkeys in self.monks.values():
            for _ in range(len(monkeys.items)):
                target, lvl = monkeys.playTurn(part)
                self.monks[target].items.append(lvl)


class Monkey:
    def __init__(self, index, items, operation, divider, tMonk, fMonk, lcm):
        self.index = index
        self.items = items
        self.operation = operation
        self.divider = divider
        self.tMonk = tMonk
        self.fMonk = fMonk
        self.turns = 0
        self.lcm = lcm
        if "+" in self.operation:
            self.op = add
        else:
            self.op = multiply

        if self.operation.split()[-1].isdigit():
            self.num = int(self.operation.split()[-1])
        else:
            self.num = None

    def playTurn(self, part):
        division = 3 if part == "1" else 1
        item = self.items.pop(0)
        num = item if self.num == None else self.num

        self.turns += 1
        lvl = self.op(item, num, self.divider)
        # print(self.divider)
        lvl = math.floor(lvl/division)

        if lvl % self.divider == 0:
            return self.tMonk, lvl % self.lcm
        else:
            return self.fMonk, lvl % self.lcm
