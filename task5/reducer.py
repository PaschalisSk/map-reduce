#!/usr/bin/python2.7
# reducer.py
import sys

prev_key = None
# We are using one reducer because the assignment states that the min and max
# should be on the same file. It would be better to use two and combine them
# through a shell script. Another way would be to have 2 jobs. In the first we
# find min and max in 2 reducers and in the second job we print them in 1 file.
min_year = None
max_year = None

for line in sys.stdin:  # For every line in the input from stdin
    line = line.strip()  # Remove trailing characters
    key, value = line.split('\t', 1)
    value = int(value)

    # If we are in the first loop set values for min and max year
    if min_year is None:
        min_year = value
        max_year = value
    else:
        if key == 'min' and value < min_year:
            min_year = value
        elif key == 'max' and value > max_year:
            max_year = value

print(str(min_year) + '\t' + str(max_year))
