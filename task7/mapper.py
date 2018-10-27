#!/usr/bin/python2.7
# mapper.py
import sys

# Variables to hold totals
total_titles = 0
total_writers = 0
# I think it's safe to assume that the memory footprint of those two numbers
# won't surpass the available RAM(practically).
# Therefore there is no need to flush.

for line in sys.stdin:
    # Extract the writers
    writers = line.strip().split('\t', 2)[2]
    # Check to see if we have at least 1 writer
    if writers != '\N':
        # Get the # of writers
        writers = len(writers.split(','))
        total_titles += 1
        total_writers += writers

print('titles\t' + str(total_titles))
print('writers\t' + str(total_writers))
# Again, each mapper outputs 2 key-value pairs. A combiner wouldn't do much.
