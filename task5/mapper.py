#!/usr/bin/python2.7
# mapper.py
import sys

# Variables to hold min and max for current mapper
min_year = None
max_year = None

for line in sys.stdin:
    # Extract the release year
    release_year = line.strip().split('\t', 8)[5]
    if release_year != '\N':
        release_year = int(release_year)
        # If it's the first loop set min and max
        if min_year is None:
            min_year = release_year
            max_year = release_year
        else:
            if release_year < min_year:
                min_year = release_year
            elif release_year > max_year:
                max_year = release_year

print('min\t' + str(min_year))
print('max\t' + str(max_year))
# Again, each mapper outputs 2 key-value pairs. A reducer wouldn't do much.
