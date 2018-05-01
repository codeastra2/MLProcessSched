from sklearn.externals import joblib

import os
import sys
import csv
import pandas
import random
import numpy as np


use_nice_model = False
if len(sys.argv) > 2:
    if sys.argv[2] == 'true':
        use_nice_model = True
if use_nice_model:
    nice_model = joblib.load('model_nice_batch_' + sys.argv[1] + '.sav')

model = joblib.load('model_' + sys.argv[1] + '.sav')
min_nice = -15
max_nice = 19
prog_rev = {"1":"bub.c", "2":"fib.c", "3":"mat.c", "4":"ms.c"}


def find_best_nice_value(row):
    min_time = 9876543210
    best_nice_value = [0, 0, 0, 0]
    row = row.reshape(1, -1)
    for nice_value in nice_value_list:
        for idx in range(0, 4):
            row[0][19 + idx*31] = nice_value[idx]
        exe_time = model.predict(row)[0]
        if exe_time < min_time:
            best_nice_value = nice_value
            min_time = exe_time
    with open('nice_value_input_' + sys.argv[1] + '.csv', 'a') as f:
        w = csv.writer(f, dialect='excel')
        nice_value_input = row[0].tolist()
        for idx in range(3, -1, -1):
            del nice_value_input[19 + idx * 31]
        nice_value_input.extend(best_nice_value)
        w.writerow(nice_value_input)
    return best_nice_value


df = pandas.read_csv('proc_dataset_isolated.csv')
array = df.values
X = array[:, 0:124]


nice_value_list = []
for i in range(int(0.4 * len(X))):      
    # Number of random values = 40% of dataset length 
    nice_value_list.append([random.randint(min_nice, 5), random.randint(min_nice, max_nice), random.randint(min_nice, 5), random.randint(min_nice, max_nice)])


new_input_list = []
counter = 1
for row in X:
    print(counter, len(X))
    counter += 1
    prog_names = []
    input_sizes = []
    for idx in range(0, 4):
        prog_names.append(prog_rev[str(row[0+31*idx])])
        input_sizes.append(row[17 + idx*31])
    if not use_nice_model:
        nice_values = find_best_nice_value(row)
    else:
        nice_value_input = row.tolist()
        for idx in range(3, -1, -1):
            del nice_value_input[19 + idx * 31]
        nice_value_input = np.asarray(nice_value_input)
        nice_value_input = nice_value_input.reshape(1, -1)
        nice_values = nice_model.predict(nice_value_input).tolist()[0]
        nice_values = [int(nice_value) for nice_value in nice_values]
    new_input = [len(new_input_list) + 1]
    for idx in range(0, 4):
        new_input.append(prog_names[idx])
        new_input.append(input_sizes[idx])
        new_input.append(nice_values[idx])
    new_input_list.append(new_input)
    new_input = [len(new_input_list) + 1]
    for idx in range(0, 4):
        new_input.append(prog_names[idx])
        new_input.append(input_sizes[idx])
        new_input.append(0)
    new_input_list.append(new_input)


with open('input.csv', 'w') as f:
    w = csv.writer(f, dialect='excel')
    for new_input in new_input_list:
        w.writerow(new_input)
