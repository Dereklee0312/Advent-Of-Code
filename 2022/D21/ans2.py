#!/usr/bin/python3

from collections import deque
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

monk1 = mathLst["root"][0]
monk2 = mathLst["root"][2]

print(monk1, monk2)

stack = deque()
stack.append((monk1, monk2))

# while stack:
#     m1, m2 = stack.popleft()
#     if m1 ==
