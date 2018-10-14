#!/usr/bin/python2.7
# combiner.py
import sys

prev_title_id = None
all_crew = ''
MAX_SIZE = 1000

for line in sys.stdin:  # For every line in the input from stdin
    line = line.strip()  # Remove trailing characters
    title_id, crew = line.split("\t", 1)

    if prev_title_id == title_id:
        # If we have exceeded our max string size print
        if len(all_crew) > MAX_SIZE:
            print(prev_title_id + "\t" + all_crew)
            all_crew = crew
        else:
            all_crew += ',' + crew
    else:
        # Write result to stdout
        if prev_title_id is not None:
            print(prev_title_id + "\t" + all_crew)

        all_crew = crew
        prev_title_id = title_id

# Don't forget the last key/value pair
if prev_title_id is not None:
    print(prev_title_id + "\t" + all_crew)
