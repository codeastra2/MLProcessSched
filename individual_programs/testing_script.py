import csv

import pandas
from sklearn.externals import joblib

filename = "model_individual.sav"
model = joblib.load(filename)

def find_best_nice_value(record):
    min_time = 9876543210
    best_nice_value = 0
    cnt = 0
    record = record.reshape(1, -1)
    #print(record)
    for nice_value in range(-20, 20):
        record[0][19] = nice_value
        exe_time = model.predict(record)[0]
        #print("!!!!!!!!!!!!!!!!!!!" + str(cnt))
        cnt = cnt + 1
        if exe_time < min_time:
            best_nice_value = nice_value
            min_time = exe_time
    return best_nice_value

prog_map = {"bub":"1", "fac":"2", "mat":"3", "hs":"4"}
prog_rev = {"1":"bub.c", "2":"fac.c", "3":"mat.c", "4":"hs.c"}
df = pandas.read_csv("dataset.csv")
array = df.values
X = array[:, 0:31]
for index in range(len(X)):
    X[index][0] = prog_map[X[index][0]]
Y = array[:, 33]

new_input_list = []
for record in X:
    prog_name = prog_rev[record[0]]
    prog_input_size = record[17]
    new_nice_value = find_best_nice_value(record)
    new_input_list.append([prog_name, prog_input_size, new_nice_value])
    new_input_list.append([prog_name, prog_input_size, 0])

with open('input.csv', 'w') as f:
    w = csv.writer(f, dialect='excel')
    for input in new_input_list:
        w.writerow(input)
