from subprocess import Popen, PIPE
import os, csv


INPUT = os.getcwd() + '/programs/'
OUTPUT = os.getcwd() + '/exe/'
codes = {}


'''
1. Writes new .c files with next set of input sizes and nice values
2. Compiles and move executables to separate folder for that set
'''
def write(values, i):
	global INPUT, OUTPUT, codes

	new_path = (OUTPUT + str(i))
	if not os.path.exists(new_path):
		os.makedirs(new_path)

	for code in codes:
		''' 1 '''
		new_code = codes[code][:]
		new_input_size = str(values[code][0])
		new_nice_value = str(values[code][1])
		new_code[8] = '#define INPUT_SIZE ' + new_input_size + '\n'
		new_code[9] = '#define NICE_VALUE ' + new_nice_value + '\n'
		name = new_path + '/' + code.split('.')[0] + '_' + new_input_size + '_' + new_nice_value + '.' + code.split('.')[1]
		with open(INPUT + code, 'w') as w:
			w.writelines(new_code)
		
		''' 2 '''
		command = 'gcc %s -o %s/%s_%s_%s' % (INPUT + code, new_path, code.split('.')[0], new_input_size, new_nice_value)
		#print command
		Popen(command, shell=True, stdout=PIPE).stdout


'''
Reads input c programs only once
'''
def read_codes():
	global INPUT, OUTPUT, codes

	for file in os.listdir(INPUT):
		pointer = open(INPUT + file)
		codes[file] = pointer.readlines()
		pointer.close()


def main():
	global INPUT, OUTPUT, codes

	if not os.path.exists(OUTPUT):
		os.makedirs(OUTPUT)

	read_codes()

	with open('input.csv', 'r') as csvfile:
		i = 1
		rows = csv.reader(csvfile)
		for row in rows:
			print ('Compiling ' + row[0])
			del row[0]
			values = {}
			values[row[0]] = [int(row[1]), int(row[2])]
			values[row[3]] = [int(row[4]), int(row[5])]
			values[row[6]] = [int(row[7]), int(row[8])]
			values[row[9]] = [int(row[10]), int(row[11])]
			values[row[12]] = [int(row[13]), int(row[14])]
			write(values, i)
			i += 1


if __name__ == "__main__":
	main()
