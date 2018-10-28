#!/usr/bin/python2.7
# mapper.py
import sys

# Empty set to hold all the genres
genres = set()
# Cap the size in case our input grows and more genres are added
MAX_SIZE = 100

for line in sys.stdin:
    # Extract all genres in a string
    title_genres = line.strip().split('\t', 8)[8]
    # Place genres in an set
    title_genres = set(title_genres.split(','))
    # If the genre is defined
    if '\N' not in title_genres:
        # Create the union of the old and new sets
        genres = genres.union(title_genres)
        if len(genres) > MAX_SIZE:
            for genre in genres:
                print('genre' + '\t' + genre)
            genres.clear()

# Print remaining genres
# One key, so everything will go to 1 reducer.
# I left  the "-D mapred.reduce.tasks=1" in the .sh in order to avoid an empty
# part-00000.
for genre in genres:
    print('genre' + '\t' + genre)

# As was the case in task3, there is no significant gain of adding
# a normal combiner in this task.
