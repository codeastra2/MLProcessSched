import csv

nice_values = []
prog_input_values = []
prog_input_map = {
    "bub.c" : {
        "start_size":1000,
        "end_size":10001,
        "step_size":4500,
        "next_prog":"fib.c"
    },
    "fib.c" : {
        "start_size":12,
        "end_size":37,
        "step_size":12,
        "next_prog":"mat.c"
    },
    "mat.c" : {
        "start_size":100,
        "end_size":701,
        "step_size":300,
        "next_prog":"ms.c"
    },
    "ms.c" : {
        "start_size":1000,
        "end_size":101001,
        "step_size":50000,
        "next_prog":"xyz"
    }
}
prog_name = ["bub.c", "fib.c", "mat.c", "ms.c"]

def nice_value_gen(index, nice_value_list):
    if index > 3:
        nice_values.append(tuple(nice_value_list))
        return
    for nice_value in range(-17,20,11):
        old_value = nice_value_list[index]
        nice_value_list[index] = nice_value
        nice_value_gen(index+1, nice_value_list)
        nice_value_list[index] = old_value
    return

def nice_value_gen_helper():
    initial_list=[21, 21, 21, 21]
    nice_value_gen(0, initial_list)
    return

def prog_input_gen(index, prog_name, prog_input_value_list):
    if index > 3:
        prog_input_values.append(tuple(prog_input_value_list))
        return

    program = prog_input_map[prog_name]
    next_prog_name = program["next_prog"]

    for prog_input_value in range(program["start_size"], program["end_size"], program["step_size"]):
        old_value = prog_input_value_list[index]
        prog_input_value_list[index] = prog_input_value
        prog_input_gen(index+1, next_prog_name, prog_input_value_list)
        prog_input_value_list[index] = old_value
    return

def prog_input_gen_helper():
    initial_list=[-1, -1, -1, -1]
    initial_prog = "bub.c"
    prog_input_gen(0, initial_prog, initial_list)
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
                    command.append(prog_name[index].split('.')[0] + ".c")
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
