# Advent Of Code
# Author: Derek Lee
# Language: Python
# Day: 1

# Part 1
calList = []
totalCal = 0
with open("test.txt") as f:
    for line in f:
        if line.startswith("\n"):
            calList.append(totalCal)
            totalCal = 0
        else:
            totalCal += int(line)

print(f'Elf with most calories has: {max(calList)}')

# Part 2
print(f'Sum of 3 elves with most calories: {sum(sorted(calList, reverse=True)[0:3])}')
