#!/usr/bin/python3

from helper import *

lines = parseFile()

monkLst = {}
mathLst = {}
removeLst = []

for line in lines:
    spl = line.split()
    if len(spl) == 2:
        monkLst[spl[0].replace(":", "")] = int(spl[1])
    else:
        mathLst[spl[0].replace(":", "")] = (spl[1], spl[2], spl[3])


while mathLst:
    removeLst.clear()
    for (key, val) in mathLst.items():
        monk1 = val[0]
        monk2 = val[2]

        if monk1 in monkLst.keys() and monk2 in monkLst.keys():
            result = compute(monkLst[monk1], monkLst[monk2], val[1])
            removeLst.append((key, result))

    for key, result in removeLst:
        mathLst.pop(key)
        monkLst[key] = result


print(monkLst["root"])
