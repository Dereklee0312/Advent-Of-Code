#!/usr/bin/python3

from helper import *

lines = parseFile()

valveSys = {}

for line in lines:
    vName = line.split()[1]
    vRate = int(line.split()[4].replace(";", "").split("=")[1])
    leads = [loc.replace(",", "") for loc in line.split()[9:]]
    valveSys[vName] = Valve(vName, vRate, leads)

for i in valveSys.values():
    print(i)
