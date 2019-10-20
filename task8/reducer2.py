#!/usr/bin/python2.7
# reducer.py
import sys

previous_decade = None
ratings_sum = 0
total_titles = 0

for line in sys.stdin:  # For every line in the input from stdin
    line = line.strip()  # Remove trailing characters
    decade, values = line.split('\t', 1)
    ratings, titles = values.split('_')
    ratings = float(ratings)
    titles = int(titles)

    if decade == previous_decade:
        ratings_sum += ratings
        total_titles += titles
    else:
        if previous_decade is not None:
            average_rating = round(ratings_sum/total_titles, 1)
            print(str(previous_decade) + '\t' + str(average_rating))

        previous_decade = decade
        ratings_sum = ratings
        total_titles = titles

# Print last pair
if previous_decade is not None:
    average_rating = round(ratings_sum/total_titles, 1)
    print(str(previous_decade) + '\t' + str(average_rating))
