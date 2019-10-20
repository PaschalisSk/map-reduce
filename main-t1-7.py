#!/usr/bin/python2.7

import sys
import os

COMBINER = False
task_folder = os.path.join('task4')
sys.path.append(task_folder)
if not os.path.exists(os.path.join(task_folder, 'outputs')):
    os.makedirs(os.path.join(task_folder, 'outputs'))
if COMBINER:
    output_file = os.path.join(task_folder, 'outputs/local_comb.out')
else:
    output_file = os.path.join(task_folder, 'outputs/local.out')

data_folder = os.path.join('exc_data', 'small', 'imdb')
input_files = [os.path.join(data_folder, 'title.basics.tsv')]

#Empty pipe
open('pipe.txt', 'w').close()

for input_file in input_files:
    with open(input_file) as sys.stdin, open('pipe.txt', 'a') as sys.stdout:
        if 'mapper' in sys.modules:
            reload(mapper)
        else:
            import mapper

with open('pipe.txt', 'r') as sys.stdin, open('sorted_pipe.txt', 'w') as sys.stdout:
    sorted_pipe = sorted(sys.stdin, key=lambda x: (x.strip().split('\t', 1)[0], x.strip().split('\t', 1)[1]))
    for entry in sorted_pipe:
        # In order not to print newline(wanted to avoid import __future__
        sys.stdout.write(entry)
    sys.stdout.flush()

if COMBINER:
    with open('sorted_pipe.txt', 'r') as sys.stdin, open('comb_pipe.txt', 'w') as sys.stdout:
        import combiner

    with open('comb_pipe.txt') as sys.stdin, open(output_file, 'w') as sys.stdout:
        import reducer
else:
    with open('sorted_pipe.txt') as sys.stdin, open(output_file, 'w') as sys.stdout:
        import reducer

sys.stdin = sys.__stdin__
sys.stdout = sys.__stdout__
print('debug_line')
