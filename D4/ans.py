# Part 1
def checkRange(first, second):
    answer = False
    firstRange = first.split("-")
    secondRange = second.split("-")

    firstList = [x for x in range(int(firstRange[0]), int(firstRange[1]) + 1)]
    secondList = [x for x in range(int(secondRange[0]), int(secondRange[1]) + 1)]

    if (set(firstList).issubset(set(secondList))) or (set(secondList).issubset(set(firstList))):
        answer = True

    return answer

def checkRange2(first, second):
    answer = False
    firstRange = first.split("-")
    secondRange = second.split("-")

    firstList = [x for x in range(int(firstRange[0]), int(firstRange[1]) + 1)]
    secondList = [x for x in range(int(secondRange[0]), int(secondRange[1]) + 1)]

    for i in firstList:
        if i in secondList:
            answer = True
    return answer

counter = 0
counter1 = 0
with open("test.txt") as f:
    for line in f:
        contents = line.strip().split(",")
        if checkRange(contents[0], contents[1]):
            counter += 1
        if checkRange2(contents[0], contents[1]):
            counter1 += 1

print(counter)
print(counter1)
