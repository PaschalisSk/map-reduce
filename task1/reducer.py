#!/usr/bin/python2.7
# reducer.py
import sys
from collections import defaultdict


prev_key = None

# Dict to store lines and words count.
# We want words to appear first but they are ordered after lines.
# So we can't just print when prev_key != key.
# The size of dict is bound at 2 since our 2 keys are 'lines' and 'words'
reducer_dict = defaultdict(int)

for line in sys.stdin:  # For every line in the input from stdin
    line = line.strip()  # Remove trailing characters
    key, value = line.split("\t", 1)
    value = int(value)

    if prev_key == key:
        reducer_dict[key] += value
    else:
        reducer_dict[key] = value
        prev_key = key

# Print the results
# if statement is required in case we didn't
# get any input (i.e. reducer_dict is empty)
if 'words' in reducer_dict and 'lines' in reducer_dict:
    print("{0}\t{1}".format(reducer_dict['words'], reducer_dict['lines']))
