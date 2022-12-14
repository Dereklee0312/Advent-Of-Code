#!/usr/bin/python3

from helper import *

lines = parseFile()
left = []
right = []

sum = 0
step = 0
num = 0

for i, line in enumerate(lines):
    if step == 0:
        left = eval(line)
        step += 1
        # print("left: ", left)
    elif step == 1:
        right = eval(line)
        # print("right: ", right)
        step += 1
    elif step == 2:
        step = 0
        num += 1
        print("STARTING COMPARISON", num)
        if compareLines(left, right) == 1:
            print("APPROVED")
            # print(num)
            sum += num
        else:
            print("DENIED")
else:
    num += 1
    print("STARTING COMPARISON", num)
    if compareLines(left, right) == 1:
        print("APPROVED")
        print(num)
        sum += num
    else:
        print("DENIED")

print(sum)
