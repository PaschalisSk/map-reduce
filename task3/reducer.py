#!/usr/bin/python2.7
# reducer.py
import sys

actors = 0

for line in sys.stdin:  # For every line in the input from stdin
    line = line.strip()  # Remove trailing characters
    key, value = line.split("\t", 1)
    actors += int(value)

print(str(actors) + '\t')
