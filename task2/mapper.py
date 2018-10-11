#!/usr/bin/python2.7
# mapper.py
import sys
from collections import defaultdict

# Dict to store lines and words count.
# We have to bound its size

bigram_dict = defaultdict(int)
MAX_SIZE = 100


def map_function(line):
    # Get the words.
    words = line.strip().split()
    # Create bigrams.
    for bigram in zip(words[:-1], words[1:]):
        yield "_".join(bigram), 1


for line in sys.stdin:
    for key, value in map_function(line):
        # Aggregate value for a bigram locally
        bigram_dict[key] += value

        # To keep O(1) space, we bound the size of our memory footprint
        if len(bigram_dict) > MAX_SIZE:
            for key, value in bigram_dict.items():
                print(key + "\t" + str(value))

            bigram_dict.clear()

# Emit remaining key-value
for key, value in bigram_dict.items():
    print(key + "\t" + str(value))
