import pandas
from sklearn import model_selection, tree
import csv


def process_op_line(line):
    op_list = line.split(',')
    op_list[0] = prog_map[op_list[0]]
    del op_list[32]
    del op_list[31]
    new_line = ",".join(op_list)
    new_line=new_line.strip()
    return new_line

def combine_lines(lines):
    net_time = 0
    comb_line = ""
    for line in lines:
        op_list = line.split(',')
        net_time += int(op_list[-1])
        del op_list[-1]
        comb_line += ",".join(op_list)
        comb_line += ","
    comb_line += str(net_time)
    return comb_line

lines = []
with open('dataset.csv', 'r') as f:
    lines = [line for line in f]

new_lines = []
programs = ["bub", "fib", "mat", "ms"]
prog_output_dict = {"bub": "", "fib": "", "mat": "", "ms": ""}
prog_map = {"bub":"1", "fib":"2", "mat":"3", "ms":"4"}
line = "*"+ ",*"*124
new_lines.append(line)
for index in range(1, len(lines), 4):
    new_line = []
    for idx in range(index, index+4):
       new_line.append(process_op_line(lines[idx]))

    new_line = combine_lines(new_line)
    new_lines.append(new_line)

with open('proc_dataset.csv', 'w') as f:
    csvwriter = csv.writer(f, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for line in new_lines:
        csvwriter.writerow(line.split())

df = pandas.read_csv("proc_dataset.csv")
array = df.values
X = array[:, 0:124]
Y = array[:, 124]
test_size = 0.33
seed = 7
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)
clf = tree.DecisionTreeRegressor(criterion="mae", splitter="random")
clf = clf.fit(X_train, Y_train)
error_percentage = ((abs(clf.predict(X_test) - Y_test)/(Y_test))*100)
print(sum(error_percentage)/len(error_percentage))