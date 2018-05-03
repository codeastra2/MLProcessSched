from sklearn.externals import joblib
from sklearn.feature_selection import VarianceThreshold

import sys
import csv
import pandas
import matplotlib.pyplot as plt

model = joblib.load('model_' + sys.argv[1] + '.sav')

prog_map = {"bub":"1", "fac":"2", "mat":"3", "hs":"4", "fib":"5", "ms":"6"}
prog_rev = {"1":"bub.c", "2":"fac.c", "3":"mat.c", "4":"hs.c", "5":"fib", "ms":"6"}
 
df = pandas.read_csv("proc_dataset_isolated.csv")
array = df.values
X = array[:, 0:31]
for index in range(len(X)):
    X[index][0] = prog_map[X[index][0]]
Y = array[:, 33]

X_copy = array[:, 0:31]
selection = VarianceThreshold()
X_copy = selection.fit_transform(X_copy)


def find_best_nice_value(row):
    min_time = 9876543210
    best_nice_value = 0
    cnt = 0
    row = row.reshape(1, -1)

    for nice_value in range(1, 20):
        row[0][10] = nice_value
        exe_time = model.predict(row)[0]
        cnt = cnt + 1
        if exe_time < min_time:
            best_nice_value = nice_value
            min_time = exe_time
    return best_nice_value


new_input_list = []
for idx,row in enumerate(X):
    prog_name = prog_rev[row[0]]
    prog_input_size = row[17]
    new_nice_value = find_best_nice_value(X_copy[idx])
    #new_nice_value = find_best_nice_value(row) - Without feature selection
    new_input_list.append([prog_name, prog_input_size, new_nice_value])
    new_input_list.append([prog_name, prog_input_size, 0])


with open('input.csv', 'w') as f:
    w = csv.writer(f, dialect='excel')
    for new_input in new_input_list:
        w.writerow(new_input)
