#!/usr/bin/python3

from helper import *

lines = parseFile()

valveSys = {}
impValves = []

for line in lines:
    vName = line.split()[1]
    vRate = int(line.split()[4].replace(";", "").split("=")[1])
    leads = [loc.replace(",", "") for loc in line.split()[9:]]
    valveSys[vName] = Valve(vName, vRate, leads)

    if vRate > 0:
        impValves.append(vName)

# for i in valveSys.values():
#     print(i)
#
# print(impValves, len(impValves))

S = ["A", "C"]
# S.append(valveSys["AA"])
visited = set()
visited.add("A")
visited.add("C")

print(visited in S)

# cont = True
# while S and True:
#     valve = S.pop(0)
#     visited.add(valve.name)
