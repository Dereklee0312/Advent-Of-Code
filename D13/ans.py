#!/usr/bin/python3

from helper import *
from functools import cmp_to_key

lines = parseFile()
sum = 0
step = 0
num = 0

lst = []

for i, line in enumerate(lines):
    if step == 0:
        left = eval(line)
        lst.append(left)
        step += 1
    elif step == 1:
        right = eval(line)
        lst.append(right)
        step += 1
    elif step == 2:
        step = 0
        num += 1
        if compareLst(left, right) == 1:
            sum += num
else:
    num += 1
    if compareLst(left, right) == 1:
        sum += num

lst.append([[2]])
lst.append([[6]])

lst = sorted(lst, key=cmp_to_key(compareLst), reverse=True)

target = [[[2]], [[6]]]

ans = 1
for i, L in enumerate(lst):
    if L in target:
        ans *= i + 1

print("P1: ", sum)
print("P2: ", ans)
