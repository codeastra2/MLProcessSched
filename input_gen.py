import copy
import csv
import random

nice_values = []
prog_input_values = []
prog_input_map = {
    "bub.c" : {
        "start_size":1000,
        "end_size":10001,
        "step_size":3000,
        "next_prog":"fib.c"
    },
    "fib.c" : {
        "start_size":29,
        "end_size":36,
        "step_size":2,
        "next_prog":"mat.c"
    },
    "mat.c" : {
        "start_size":100,
        "end_size":341,
        "step_size":80,
        "next_prog":"ms.c"
    },
    "ms.c" : {
        "start_size":10000,
        "end_size":100001,
        "step_size":30000,
        "next_prog":"xyz"
    }
}
nice_value_dict = {
    "start": -18,
    "end": 18
}
prog_names = ["bub.c", "fib.c", "mat.c", "ms.c"]

def nice_value_gen(nice_values_num):
    for index in range(nice_values_num):
        nice_value_list = []
        for nice_index in range(0, 4):
            nice_value_list.append(random.randint(nice_value_dict["start"],
                                                  nice_value_dict["end"]))
        nice_values.append(copy.deepcopy(nice_value_list))
    return

def nice_value_gen_helper():
    nice_values_num = 6**4
    nice_value_gen(nice_values_num)
    return

def prog_input_gen(prog_input_num):
    for index in range(0, prog_input_num):
        prog_input_value_list = []
        for prog_name in prog_names:
            start = prog_input_map[prog_name]["start_size"]
            end = prog_input_map[prog_name]["end_size"]
            prog_input_value_list.append(random.randint(start, end))
        prog_input_values.append(copy.deepcopy(prog_input_value_list))
    return

def prog_input_gen_helper():
    prog_input_num = (160000)/(6**4)
    prog_input_gen(prog_input_num)
    return

def write_to_csv():
    with open('input.csv', 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        dataset_index = 1
        for nice_value in nice_values:
            for prog_input_value in prog_input_values:
                command = []
                command.append(dataset_index)
                for index in range(0,len(prog_input_value)):
                    command.append(prog_names[index].split('.')[0] + ".c")
                    command.append(prog_input_value[index])
                    command.append(nice_value[index])
                filewriter.writerow(command)
                dataset_index = dataset_index + 1
    return

def main():
    print("Generating the Nice values...")
    nice_value_gen_helper()
    print(len(nice_values))

    print("Generating the input values for programs...")
    prog_input_gen_helper()
    print(len(prog_input_values))

    print("Writing the dataset to CSV file...")
    write_to_csv()

if __name__== "__main__":
  main()
