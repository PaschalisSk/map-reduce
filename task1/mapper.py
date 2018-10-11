#!/usr/bin/python2.7
# mapper.py
import sys
from collections import defaultdict

# Dict to store lines and words count.
# No reason to bound its size since it will only have 2 keys (lines, words)
mapper_dict = defaultdict(int)

for line in sys.stdin:
    mapper_dict["lines"] += 1
    mapper_dict["words"] += len(line.strip().split())

# Emit key-value pairs and use '\t' as the delimiter
for key, value in mapper_dict.items():
    print(key + "\t" + str(value))
