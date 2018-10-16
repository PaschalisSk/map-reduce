#!/usr/bin/python2.7
# mapper.py
import sys

# Array to hold sum of scores for each decade
# Array has practically constant size
# Index 0 for 1900, 1 for 1910 etc.
# Can't initialize to 0 because it is a valid rating
scores_sum = [None] * 10
# Array to hold count of titles for each decade
titles_count = [None] * 10

for line in sys.stdin:
    year, rating = line.strip().split('\t', 1)
    year = int(year)
    rating = float(rating)
    year_index = (year % 100) / 10
    # If array element for that year is None set it to current value, else
    # increment accordingly.
    if titles_count[year_index] is None:
        scores_sum[year_index] = rating
        titles_count[year_index] = 1
    else:
        scores_sum[year_index] += rating
        titles_count[year_index] += 1

# For every index i.e. decade
for i in range(10):
    # If we found ratings in this decade
    if titles_count[i] is not None:
        # Sample output: 1930   13.2_3
        print('19' + str(i) + '0\t' + str(scores_sum[i]) + '_' + str(
            titles_count[i]))
