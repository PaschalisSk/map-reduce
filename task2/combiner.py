#!/usr/bin/python2.7
# combiner.py
import sys

# Although we have an in-map combiner we also have a normal one
# because our mapper produces partial results and also we could have
# more than one mapper in one machine.
prev_bigram = None
value_total = 0

for line in sys.stdin:  # For every line in the input from stdin
    line = line.strip()  # Remove trailing characters
    bigram, value = line.split("\t", 1)
    value = int(value)

    if prev_bigram == bigram:
        value_total += value
    else:
        # Write result to stdout
        if prev_bigram is not None:
            print(prev_bigram + "\t" + str(value_total))

        value_total = value
        prev_bigram = bigram

# Don't forget the last key/value pair
if prev_bigram is not None:
    print(prev_bigram + "\t" + str(value_total))
