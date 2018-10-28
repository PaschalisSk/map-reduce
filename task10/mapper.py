#!/usr/bin/python2.7
# mapper.py
import sys

for line in sys.stdin:
    parts = line.strip().split('\t')

    if len(parts) == 9:  # We're processing a line from title.basics.tsv
        # If year column has value
        if parts[5] != '\N':
            # If year is between our range
            if 2010 <= int(parts[5]) <= 2018:
                title_id = parts[0]
                print(title_id + '\t' + 'c')
    else:  # We're processing a line from name.basics.tsv
        # If the person has knownForTitle
        if parts[5] != '\N':
            crew_id = parts[0]
            titles = parts[5].split(',')
            for title_id in titles:
                print(title_id + '\t' + crew_id)
