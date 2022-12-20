#!/usr/bin/python3

from helper import *

lines = parseFile()

nums = []
nums2 = []
for line in lines:
    nums.append([False, int(line)])
    nums2.append(int(line))

for i, num in enumerate(nums2):
    index = nums.index([False, num])

    nums[index][0] = True
    removed = nums.pop(index)
    to = removed[1]

    if abs(to) >= len(nums):
        to %= len(nums)

    if 0 < index + to <= len(nums) - 1:
        index += to
    elif index + to < 0:
        index += to + len(nums)
    elif index + to == 0:
        index = len(nums)
    else:
        index += to - len(nums)

    nums.insert(index, removed)
    # print(f"AFTER moving {removed[1]}: ")
    # print(nums, index, index+removed[1])
    # print("")
    # print(nums)

xLst = [y for _, y in nums]

zero = xLst.index(0)

sum = 0

sum += xLst[whatNum(xLst, zero, 1000)]
sum += xLst[whatNum(xLst, zero, 2000)]
sum += xLst[whatNum(xLst, zero, 3000)]

print(sum)
