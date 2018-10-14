#!/usr/bin/python2.7
# mapper.py
import sys
from collections import defaultdict

# Dict to store releases for each genre
# Practically, for our case, we don't have many genres
# so no need to flush
mapper_dict = defaultdict(int)

for line in sys.stdin:  # For every line in the input from stdin
    parts = line.strip().split('\t')

    # If year and genre columns have value
    if parts[5] != '\N' and parts[8] != '\N':
        # If year is between our range
        if 2000 <= int(parts[5]) <= 2014:
            genres = parts[8].split(',')
            for genre in genres:
                mapper_dict[genre] += 1

# Emit key-value pairs and use '\t' as the delimiter
for key, value in mapper_dict.items():
    print(key + "\t" + str(value))

# Again, a normal combiner in this task would only combine outputs
# from different mappers in one machine and since each mapper
# produces a small amount ( <=28 as we saw in task4) of key-value pairs
# it wouldn't add much.
