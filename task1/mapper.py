#!/usr/bin/python2.7
# mapper.py
import sys

# Variables to store line count and word count
lines = 0
words = 0

for line in sys.stdin:
    lines += 1
    words += len(line.strip().split())

# Emit key-value pairs and use '\t' as the delimiter
print("lines" + "\t" + str(lines))
print("words" + "\t" + str(words))

# Both in this and some of the next tasks we implement a combiner
# only to combine results from multiple mappers in one machine.
