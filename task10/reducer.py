#!/usr/bin/python2.7
# reducer.py
import sys

prev_title_id = None
# The lines with titles within our year range (2010-2018)
# are sorted before the ones with crew id because they have 'c' in the second
# column. We can therefore check the year column for a new title_id and if
# the column has value='c' then this movie was released 2010-2018.
valid_year = False

for line in sys.stdin:  # For every line in the input from stdin
    title_id, crew_id = line.strip().split('\t', 1)

    # We are reading lines ordered by 1)title_id and 2)crew_id
    if prev_title_id == title_id:
        if valid_year:
            print(crew_id + '\t')
    else:
        if crew_id == 'c':
            valid_year = True
        else:
            valid_year = False

        prev_title_id = title_id

# We can't miss any crew_id so there is nothing here.
# If a crew_id is to be printed, it will be printed inside the
# if statement which checks for valid_year
