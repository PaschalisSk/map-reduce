#!/usr/bin/python2.7
# mapper.py
import sys

# Empty set to hold all the genres
genres = set()

for line in sys.stdin:
    # Extract all genres in a string
    title_genres = line.strip().split('\t', 8)[8]
    # Place genres in an set
    title_genres = set(title_genres.split(','))
    # If the genre is defined
    if '\N' not in title_genres:
        # Create the union of the old and new sets
        genres = genres.union(title_genres)

# It's going to be a long string with all the genres but
# for our problem an upper bound of 100 genres, each 10 characters long,
# is logical. Hence, we don't have to flush incomplete results.
# Thankfully we are handling movie genres and not music so we are
# avoiding stuff like every possible combination of post, nu, alternative,
# experimental, progressive, experimental metal :)
print('genres' + '\t' + ','.join(genres))

# As was the case in task3, there is no significant gain of adding
# a normal combiner in this task.
