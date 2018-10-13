#!/usr/bin/python2.7
# mapper.py
import sys

# Variables to hold totals
total_titles = 0
total_votes = 0
# I think it's safe to assume that the memory footprint of those two numbers
# won't surpass the available RAM(practically).
# Therefore there is no need to flush.
# In the log I found: Map output materialized bytes = 80
# So we are way more than fine.

for line in sys.stdin:
    # Extract the total votes
    votes = line.strip().split('\t', 2)[2]
    # numvotes is not optional so no need to check for \N
    total_titles += 1
    total_votes += int(votes)

print('titles\t' + str(total_titles))
print('votes\t' + str(total_votes))
# Again, each mapper outputs 2 key-value pairs. A reducer wouldn't do much.
