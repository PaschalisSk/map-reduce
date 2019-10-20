#!/usr/bin/python2.7
# mapper.py
import sys
from collections import defaultdict

# Dict to store releases for each genre
# Practically, for our case, we don't have many genres.
# In task 4 we found that we have 28 genres.
# However we will still flush for good practice.
mapper_dict = defaultdict(int)
MAX_SIZE = 100

for line in sys.stdin:  # For every line in the input from stdin
    parts = line.strip().split('\t')

    # If year and genre columns have value
    if parts[5] != '\N' and parts[8] != '\N':
        # If year is between our range
        if 2000 <= int(parts[5]) <= 2014:
            genres = parts[8].split(',')
            for genre in genres:
                mapper_dict[genre] += 1
                if len(mapper_dict) > MAX_SIZE:
                    for key, value in mapper_dict.items():
                        print(key + "\t" + str(value))
                    mapper_dict.clear()

# Emit remaining key-value pairs and use '\t' as the delimiter
for key, value in mapper_dict.items():
    print(key + "\t" + str(value))
