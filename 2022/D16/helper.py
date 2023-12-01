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

class Valve:
    def __init__(self, name, rate, leads):
        self.name = name
        self.rate = rate
        self.leadTo = leads

    def __str__(self):
        return f"Name: {self.name} \t Rate: {self.rate} \t Leads To: {self.leadTo}"
