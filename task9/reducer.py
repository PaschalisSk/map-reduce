#!/usr/bin/python2.7
# reducer.py
import sys

prev_genre = None
value_total = 0

for line in sys.stdin:  # For every line in the input from stdin
    genre, value = line.strip().split("\t", 1)
    value = int(value)

    # Remember that Hadoop sorts mapper output by key,
    # and the reducer takes these keys sorted
    if prev_genre == genre:
        value_total += value
    else:
        # Write result to stdout
        if prev_genre is not None:
            # Space between bigram and values, tab afterwards.
            # Weird but that was the sample output structure.
            print(prev_genre + '\t' + str(value_total))

        value_total = value
        prev_genre = genre

# Don't forget the last key/value pair
if prev_genre is not None:
    print(prev_genre + '\t' + str(value_total))
