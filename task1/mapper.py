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

# We could add a combiner in order to combine outputs from different
# mappers which run in the same machine. However, the large Gutenberg dataset
# has only 17 files which means the best increase we could get from a
# reducer is if those 17 mappers(1 for each file) run on the same machine.
# i.e. In the best case, a machine would shuffle & short 2 key-pair values
# instead of 34(each mapper outputs 2 key-pair values). It is an infinitesimal
# increase for this dataset so we didn't implement a combiner.
