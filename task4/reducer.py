#!/usr/bin/python2.7
# reducer.py
import sys

# Set which holds all the sets
# Again, given our problem, we won't have memory problems, so we are not
# flushing.
genres = set()

for line in sys.stdin:  # For every line in the input from stdin
    line = line.strip()  # Remove trailing characters
    key, value = line.split('\t', 1)
    value = set(value.split(','))
    genres = genres.union(value)

for genre in sorted(genres):
    # Here, and in some previous examples, I am adding the \t just to match the
    # sample output.
    print(genre + '\t')
