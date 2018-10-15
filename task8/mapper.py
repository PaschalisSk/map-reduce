#!/usr/bin/python2.7
# mapper.py
import math
import sys

# If the mapper reads from title.basics.tsv it will produce pairs of the form
# title_id    decade    'r'
# If the mapper reads from title.ratings.tsv it will produce pairs of the form
# title_id    'y'    rating
# The reducer will read pairs with the same key(title_id) and create pairs
# decade     rating
# That way the second job will be able to find the average for each decade
for line in sys.stdin:
    parts = line.strip().split('\t')

    if len(parts) == 9:  # We're processing a line from title.basics.tsv
        # If year column has value
        if parts[5] != '\N':
            # If year is between our range
            if 1900 <= int(parts[5]) <= 1999:
                title_id = parts[0]
                # We care about decades, so we may as well floor
                # the year down to the decade
                year = int(parts[5])
                year = int(math.floor(year / 10.0) * 10)
                print(title_id + '\t' + str(year) + '\t' + 'r')
    else:  # We're processing a line from title.ratings.tsv
        title_id = parts[0]
        rating = parts[1]
        print(title_id + '\t' + 'y' + '\t' + rating)
