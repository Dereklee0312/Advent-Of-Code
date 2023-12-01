#!/usr/bin/python3

from helper import *

lines = parseFile()

nums = []
for i, line in enumerate(lines):
    nums.append([i, int(line) * 811589153])

nums2 = nums.copy()
for _ in range(10):
    mix(nums, nums2)

xLst = [y for _, y in nums]

zero = xLst.index(0)

sum = 0

print(xLst[whatNum(xLst, zero, 1000)])
print(xLst[whatNum(xLst, zero, 2000)])
print(xLst[whatNum(xLst, zero, 3000)])

sum += xLst[whatNum(xLst, zero, 1000)]
sum += xLst[whatNum(xLst, zero, 2000)]
sum += xLst[whatNum(xLst, zero, 3000)]

print(sum)
