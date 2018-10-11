#!/usr/bin/python2.7

import sys
import os

task_folder = os.path.join('task2')
sys.path.append(task_folder)
if not os.path.exists(os.path.join(task_folder, 'outputs')):
    os.makedirs(os.path.join(task_folder, 'outputs'))
output_file = os.path.join(task_folder, 'outputs/local_comb.out')

data_folder = os.path.join('exc_data', 'small', 'gutenberg')
input_files = [os.path.join(data_folder, '8830902613096153013.txt'),
               os.path.join(data_folder, '8849603765382661967.txt'),
               os.path.join(data_folder, '8920594670119951108.txt')]

#Empty pipe
open('pipe.txt', 'w').close()

for input_file in input_files:
    with open(input_file) as sys.stdin, open('pipe.txt', 'a') as sys.stdout:
        if 'mapper' in sys.modules:
            reload(mapper)
        else:
            import mapper

with open('pipe.txt', 'r') as sys.stdin, open('sorted_pipe.txt', 'w') as sys.stdout:
    sorted_pipe = sorted(sys.stdin, key=lambda x: x.strip().split('\t', 1)[0])
    for entry in sorted_pipe:
        # In order not to print newline(wanted to avoid import __future__
        sys.stdout.write(entry)
    sys.stdout.flush()

with open('sorted_pipe.txt', 'r') as sys.stdin, open('comb_pipe.txt', 'w') as sys.stdout:
    import combiner

with open('comb_pipe.txt') as sys.stdin, open(output_file, 'w') as sys.stdout:
    import reducer

# with open('sorted_pipe.txt') as sys.stdin, open(output_file, 'w') as sys.stdout:
#     import reducer

sys.stdin = sys.__stdin__
sys.stdout = sys.__stdout__
print('debug_line')
