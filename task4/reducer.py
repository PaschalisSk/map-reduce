#!/usr/bin/python2.7
# reducer.py
import sys

prev_genre = None

for line in sys.stdin:  # For every line in the input from stdin
    line = line.strip()  # Remove trailing characters
    key, genre = line.split('\t', 1)

    # We have one key ('genre') and the inputs are listed based on the
    # values so we already have the required alphabetical order.
    if genre != prev_genre:
        # Print every new genre we read
        print(genre + '\t')
        prev_genre = genre
