from subprocess import Popen, PIPE
from datetime import datetime
import os, shutil, csv


INPUT = os.getcwd() + '/programs/'
OUTPUT = os.getcwd() + '/exe/'
ERROR = os.getcwd() + '/error/'
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

	try:
		for code in codes:
			''' 1 '''
			new_code = codes[code][:]
			new_input_size = str(values[code][0])
			new_nice_value = str(values[code][1])

			''' Line numbers 9 and 10 in .c files '''
			new_code[8] = '#define INPUT_SIZE ' + new_input_size + '\n'
			new_code[9] = '#define NICE_VALUE ' + new_nice_value + '\n'
			
			with open(INPUT + code, 'w') as w:
				w.writelines(new_code)
			
			''' 2 '''
			command = 'gcc %s -o %s/%s_%s_%s' % (INPUT + code, new_path, code.split('.')[0], new_input_size, new_nice_value)
			#print command
			#sub = Popen(command, shell=True, stdout=PIPE)
			
			if Popen(command, stdout=PIPE, stderr = PIPE, shell = True).communicate()[1] != '':
				raise Exception('Error in gcc')			

	except Exception as e:
		print(e)
		shutil.rmtree(new_path)
		with open(ERROR + 'error.txt', 'a') as f:
			f.write(str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S")) + '\t' + 'Compiling\t' + str(i) + '\t' + str(e) + '\n')


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
	
	''' Deletes existing exe folder, if any '''
	if os.path.exists(OUTPUT):
		shutil.rmtree(OUTPUT)
	os.makedirs(OUTPUT)

	if not os.path.exists(ERROR):
		os.makedirs(ERROR)

	read_codes()
	
	''' Range to be entered by user. It corresponds to row id in input.csv '''

	start, end = raw_input('Enter start and end index (both inclusive) to run\n').split(' ')
	start = int(start)
	end = int(end)

	with open('input.csv', 'r') as csvfile:
		i = 1
		rows = csv.reader(csvfile)
		
		for row in rows:
			''' Compiles programs within the input range '''
			if i >= start and i<=end:
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
