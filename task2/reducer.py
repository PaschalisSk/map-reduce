#!/usr/bin/python2.7
# reducer.py
import sys

prev_bigram = None
value_total = 0

for line in sys.stdin:  # For every line in the input from stdin
    line = line.strip()  # Remove trailing characters
    bigram, value = line.split("\t", 1)
    value = int(value)

    # Remember that Hadoop sorts mapper output by key,
    # and the reducer takes these keys sorted
    if prev_bigram == bigram:
        value_total += value
    else:
        # Write result to stdout
        if prev_bigram is not None and value_total > 5:
            # Space between bigram and values, tab afterwards.
            # Weird but that was the sample output structure.
            print("{0} {1}\t".format(prev_bigram, value_total))

        value_total = value
        prev_bigram = bigram

# Don't forget the last key/value pair
# I have 'prev_bigram is not None' instead of 'prev_bigram == bigram' which
# was in lab 2. This is because maybe the input files are empty
# and bigram is not initialised. The final result is the same
if prev_bigram is not None and value_total > 5:
    print("{0} {1}\t".format(prev_bigram, value_total))
