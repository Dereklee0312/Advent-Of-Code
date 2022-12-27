import sys


def parseFile():
    if len(sys.argv) == 1:
        filename = "demo.txt"
    else:
        filename = "input.txt"

    lines = []
    with open(filename) as f:
        for line in f:
            lines.append(line.strip())

    return lines


"""
Have to ensure all mathematical monkeys have already given an answer
Can loop through each monkeys, those that have given their number are removed from list
"""


def compute(monk1: int, monk2: int, op: str):
    if op == "+":
        return monk1 + monk2

    elif op == "-":
        return monk1 - monk2

    elif op == "*":
        return monk1 * monk2

    elif op == "/":
        return monk1 / monk2

def giveSecond(given: str, inp: tuple):
    if inp[0] == given:
        return inp[2]
    else:
        return inp[0]
