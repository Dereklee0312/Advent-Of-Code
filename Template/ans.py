#!/usr/bin/python3

from helper import *

lines = parseFile()

for line in lines:
    print(list(enumerate(line.split())))
