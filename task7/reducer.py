#!/usr/bin/python2.7
# reducer.py
import sys

# Variables to hold totals
total_titles = 0
total_writers = 0

for line in sys.stdin:  # For every line in the input from stdin
    line = line.strip()  # Remove trailing characters
    key, value = line.split('\t', 1)
    value = int(value)

    if key == 'titles':
        total_titles += value
    elif key == 'writers':
        total_writers += value

float_result = round(total_writers/float(total_titles))
print(str(int(float_result)) + '\t')
