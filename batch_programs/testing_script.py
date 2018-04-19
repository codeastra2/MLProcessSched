from sklearn.externals import joblib

import sys
import csv
import pandas
import random

filename = 'model_' + sys.argv[1] +'.sav'
model = joblib.load(filename)
min_nice = -15
max_nice = 19

prog_rev = {"1":"bub.c", "2":"fib.c", "3":"mat.c", "4":"ms.c"}
nice_value_list = []
for i in range(50):
    nice_value_list.append([random.randint(min_nice, max_nice), random.randint(min_nice, max_nice), random.randint(min_nice, max_nice), random.randint(min_nice, max_nice)])


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
    return best_nice_value


df = pandas.read_csv("proc_dataset.csv")
array = df.values
X = array[:, 0:124]


new_input_list = []
for row in X:
    prog_names = []
    input_sizes = []
    for idx in range(0, 4):
        prog_names.append(prog_rev[str(row[0+31*idx])])
        input_sizes.append(row[17 + idx*31])
    nice_values = find_best_nice_value(row)
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
