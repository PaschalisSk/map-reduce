#!/usr/bin/python2.7
# reducer.py
import sys

# We could have secondary ordering and the code here would be simpler.
# However, I didn't think about it and completed the task this way.
# The concept is that if we read two lines with the same title_id
# then we have both a valid decade and a rating for that title.
prev_title_id = None
year = None
rating = None

for line in sys.stdin:  # For every line in the input from stdin
    line = line.strip()  # Remove trailing characters
    title_id, value = line.split('\t', 1)

    # We are reading lines ordered by title_id
    if prev_title_id == title_id:
        # If we found two equal title_id then we have both the year and the
        # rating of the title so we are printing. If we read the rating
        # in the previous line we are now reading the year and vice versa.
        if value.split('\t')[0] != 'y':
            year = value.split('\t')[0]
        else:
            rating = value.split('\t')[1]
        print(year + '\t' + rating)
    else:
        # If the first line of the new title_id is the year we are saving the
        # year and resetting rating to None and vice versa
        if value.split('\t')[0] != 'y':
            year = value.split('\t')[0]
            rating = None
        else:
            rating = value.split('\t')[1]
            year = None

        prev_title_id = title_id

# We can't miss any pairs so there is nothing here.
# If a pair is to be printed, it will be printed inside the
# if statement which checks "prev_title_id == title_id"
