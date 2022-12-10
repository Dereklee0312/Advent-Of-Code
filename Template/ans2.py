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
