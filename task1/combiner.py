#!/usr/bin/python2.7
# combiner.py
import sys

# Generic combiner used in multiple tasks to sum results
# from multiple mappers in one machine.
# prev_key = None
# values_sum = 0
#
# for line in sys.stdin:
#     key, value = line.strip().split("\t", 1)
#     value = int(value)
#
#     if prev_key == key:
#         values_sum += value
#     else:
#         # Write result to stdout
#         if prev_key is not None:
#             print(prev_key + "\t" + str(values_sum))
#
#         values_sum = value
#         prev_key = key
#
# # Don't forget the last key/value pair
# if prev_key is not None:
#     print(prev_key + "\t" + str(values_sum))

wc = 0
lc = 0

for line in sys.stdin:
    key, value = line.strip().split("\t", 1)
    value = int(value)

    if key == 'lines':
        lc += value
    else:
        wc += value
        
# Don't forget the last key/value pair
print('lines' + "\t" + str(lc))
print('words' + "\t" + str(wc))
