#!/usr/bin/python2.7
# mapper.py
import sys

# Variables to hold totals
total_titles = 0
total_votes = 0

for line in sys.stdin:
    # Extract the total votes
    votes = line.strip().split('\t', 2)[2]
    # numvotes is not optional so no need to check for \N
    total_titles += 1
    total_votes += int(votes)

print('titles\t' + str(total_titles))
print('votes\t' + str(total_votes))
# Again, each mapper outputs 2 key-value pairs. A reducer wouldn't do much.
