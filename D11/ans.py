#!/usr/bin/python3

from helper import *


lines = parseFile()

stop = 5
start = 0
monkLst = MonkeyLst()
for index, cmd in enumerate(lines):
    if index <= stop:
        if start == 0:
            cmd = cmd.replace(":", "")
            monkIndex = int(cmd.split()[1])
        elif start == 1:
            startItems = cmd.split(":")
            items = [int(a) for a in startItems[1].split(",")]
        elif start == 2:
            operation = cmd.split("=")[1].strip()
        elif start == 3:
            divider = int(cmd.split()[-1])
        elif start == 4:
            tMonk = int(cmd.split()[-1])
        elif start == 5:
            fMonk = int(cmd.split()[-1])
        start += 1
    else:
        monkey = Monkey(monkIndex, items, operation, divider, tMonk, fMonk)
        monkLst.addMonk(monkey)
        start = 0
        stop += 7

monkey = Monkey(monkIndex, items, operation, divider, tMonk, fMonk)
monkLst.addMonk(monkey)

roundLst = [19, 999, 1999, 2999, 3999, 4999, 5999, 6999, 7999, 8999, 9999]
for i in range(20):
    # print(i)
    monkLst.playRound()

turnLst = sorted([i.turns for i in monkLst.monks.values()], reverse=True)
print(turnLst[0] * turnLst[1])
