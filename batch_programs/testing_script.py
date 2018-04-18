import csv

from sklearn.externals import joblib
import pandas

filename = "model_batch.sav"
model = joblib.load(filename)

prog_rev = {"1":"bub.c", "2":"fib.c", "3":"mat.c", "4":"ms.c"}
nice_values = [-15, -7, 0, 7, 15]
nice_value_list = []
for val1 in nice_values:
    for val2 in nice_values:
        for val3 in nice_values:
            for val4 in nice_values:
                nice_value_list.append([val1, val2, val3, val4])

def find_best_nice_value(record):
    min_time = 9876543210
    best_nice_value = [0, 0, 0, 0]
    record = record.reshape(1, -1)
    for nice_value in nice_value_list:
        for idx in range(0, 4):
            record[0][19 + idx*31] = nice_value[idx]
        exe_time = model.predict(record)[0]
        if exe_time < min_time:
            best_nice_value = nice_value
            min_time = exe_time
    return best_nice_value


df = pandas.read_csv("proc_dataset.csv")
array = df.values
X = array[:, 0:124]
new_input_list = []
for record in X:
    prog_names = []
    input_sizes = []
    for idx in range(0, 4):
        prog_names.append(prog_rev[str(record[0+31*idx])])
        input_sizes.append(record[17 + idx*31])
    nice_values = find_best_nice_value(record)
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

#print(new_input_list)
with open('input.csv', 'w') as f:
    w = csv.writer(f, dialect='excel')
    for input in new_input_list:
        w.writerow(input)


