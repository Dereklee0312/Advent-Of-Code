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

print(max(calList))

# Part 2
print(sum(sorted(calList, reverse=True)[0:3]))
