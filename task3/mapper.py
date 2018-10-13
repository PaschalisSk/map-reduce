#!/usr/bin/python2.7
# mapper.py
import sys

actors = 0

for line in sys.stdin:
    profession = line.split('\t', 5)[4]
    # No need to check for \N, the condition below accounts for it
    if 'actor' in profession or 'actress' in profession:
        actors += 1

print('actors' + "\t" + str(actors))

# The gains of a normal combiner in this task would be minimal
# From the log we can see that there are 4 map output records so
# best case scenario is to combine 4 key-value pairs in 1.
