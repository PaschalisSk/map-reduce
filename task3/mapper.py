#!/usr/bin/python2.7
# mapper.py
import sys
from collections import defaultdict


actors = 0

for line in sys.stdin:
    profession = line.split('\t', 5)[4]
    if 'actor' in profession or 'actress' in profession:
        actors += 1

print('actors' + "\t" + str(actors))
