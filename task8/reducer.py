#!/usr/bin/python2.7
# reducer.py
import sys

prev_title_id = None
year = None
rating = None

for line in sys.stdin:  # For every line in the input from stdin
    line = line.strip()  # Remove trailing characters
    title_id, value = line.split('\t', 1)

    # We are reading lines ordered by 1) title_id and 2) year since 'y' > [0-9]
    # the line with the year will be sorted before the one with the rating
    if prev_title_id == title_id:
        # If we found two equal titles then we have both the year and the
        # rating of the title so we are printing. We have the year from the
        # previous line and we are now getting the rating
        rating = value.split('\t')[1]
        print(year + '\t' + rating)
    else:
        # If it's the first line of this title and it's a rating line it means
        # that we don't have the year of this title so we just move on.
        # Note that a rating's line has 'y' in the year column
        if value.split('\t')[0] != 'y':
            year = value.split('\t')[0]

        prev_title_id = title_id

# We can't miss any pairs so there is nothing here.
# If a pair is to be printed, it will be printed inside the
# if statement which checks "prev_title_id == title_id"
