#!/usr/bin/python2.7
# reducer.py
import sys

prev_bigram = None
value_total = 0

for line in sys.stdin:  # For ever line in the input from stdin
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
if prev_bigram is not None and value_total > 5:
    print("{0} {1}\t".format(prev_bigram, value_total))
