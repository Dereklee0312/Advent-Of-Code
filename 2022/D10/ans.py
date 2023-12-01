#!/usr/bin/python3
import sys

if len(sys.argv) == 1:
    filename = "demo.txt"
else:
    filename = "input.txt"

lines = []
with open(filename) as f:
    for line in f:
        lines.append(line.strip())

Xval = 1
cycle = 0
intSignals = [20, 60, 100, 140, 180, 220]
signals = {"noop": 1, "addx": 2}
signalLst = []

for cmd in lines:
    signal = cmd.split()[0]
    for _ in range(signals[signal]):
        cycle += 1
        if cycle in intSignals:
            signalLst.append(cycle * Xval)

    if len(cmd.split()) == 2:
        value = int(cmd.split()[1])
        Xval += value

print(sum(signalLst))
