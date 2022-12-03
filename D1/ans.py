# Advent Of Code
# Author: Derek Lee
# Language: Python
# Day: 1

calList = []
totalCal = 0
with open("test.txt") as f:
    for line in f:
        # Reset the totalCal to 0 as new Elf is entering data
        if line.startswith("\n"):
            calList.append(totalCal)
            totalCal = 0
        else:
            totalCal += int(line)

# Part 1
print(f'Elf with most calories has: {max(calList)}')

# Part 2
print(f'Sum of 3 elves with most calories: {sum(sorted(calList, reverse=True)[0:3])}')
