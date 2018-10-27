#!/usr/bin/python2.7
# mapper.py
import sys

# Variables to store line count and word count
lines = 0
words = 0

for line in sys.stdin:
    lines += 1
    words += len(line.strip().split())

# Emit key-value pairs and use '\t' as the delimiter
print("lines" + "\t" + str(lines))
print("words" + "\t" + str(words))

# Both in this and some of the next tasks we implement a combiner
# only to combine results from multiple mappers in one machine.

# We could add a combiner in order to combine outputs from different
# mappers which run in the same machine. However, the large Gutenberg dataset
# has only 17 files which means the best increase we could get from a
# reducer is if those 17 mappers(1 for each file) run on the same machine.
# i.e. In the best case, a machine would shuffle & short 2 key-pair values
# instead of 34(each mapper outputs 2 key-pair values). It is an infinitesimal
# increase for this dataset so we didn't implement a combiner.

