#!/usr/bin/python3

# module to deep copy a list
import copy

from helper import *

lines = parseFile()

lcm = 1
for cmd in lines:
    if "divisible" in cmd:
        lcm *= int(cmd.split()[-1])

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
        monkey = Monkey(monkIndex, items, operation, divider, tMonk, fMonk, lcm)
        monkLst.addMonk(monkey)
        start = 0
        stop += 7

else:
    monkey = Monkey(monkIndex, items, operation, divider, tMonk, fMonk, lcm)
    monkLst.addMonk(monkey)

monkLst2 = copy.deepcopy(monkLst)

# PART 1
for i in range(20):
    monkLst.playRound("1")

turnLst = sorted([i.turns for i in monkLst.monks.values()], reverse=True)
print("Part 1:", turnLst[0] * turnLst[1])

# PART 2
for i in range(10000):
    monkLst2.playRound("2")

turnLst = sorted([i.turns for i in monkLst2.monks.values()], reverse=True)
print("Part 2:", turnLst[0] * turnLst[1])
