#!/usr/bin/python2.7
# mapper.py
import sys

# Variables to hold min and max for current mapper
total_titles = 0
total_votes = 0
# I think it's safe to assume that the memory footprint of those two numbers
# won't surpass the available RAM. Therefore there is no need to flush.

for line in sys.stdin:
    # Extract the total votes
    votes = line.strip().split('\t', 2)[2]
    # Check to see if the number is given. Just to be safe
    if votes != '\N':
        total_titles += 1
        total_votes += int(votes)

print('titles\t' + str(total_titles))
print('votes\t' + str(total_votes))
# Again, each mapper outputs 2 key-value pairs. A reducer wouldn't do much.
