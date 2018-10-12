#!/usr/bin/python2.7
# reducer.py
import sys

total_titles = 0
total_votes = 0

for line in sys.stdin:  # For every line in the input from stdin
    line = line.strip()  # Remove trailing characters
    key, value = line.split('\t', 1)
    value = int(value)

    if key == 'titles':
        total_titles += value
    elif key == 'votes':
        total_votes += value

print(str(round(total_votes/float(total_titles), 2)) + '\t')
