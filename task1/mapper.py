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

# We could add a combiner in order to combine outputs from different
# mappers which run in the same machine. However, the large Gutenberg dataset
# has only 17 files which means the best increase we could get from a
# reducer is if those 17 mappers(1 for each file) run on the same machine.
# i.e. In the best case, a machine would shuffle & short 2 key-pair values
# instead of 34(each mapper outputs 2 key-pair values). It is an infinitesimal
# increase for this dataset so we didn't implement a combiner.

# I later added a combiner, even if it wouldn't change much, and you can find
# it at combiner.py. However, for some reason, I saw in the log that the
# combine input was equal to the combine output. So for some reason the
# combiner didn't do anything and only added overhead. Therefore, I removed it
# from run.sh. I also tried it in task3 but with the same results. If the
# combiner had any results it could be added to tasks 1, 3, 4, 6, 7, and 9.
