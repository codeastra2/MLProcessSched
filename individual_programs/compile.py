from subprocess import Popen, PIPE
from datetime import datetime
import os
import shutil
import csv
import itertools
import random
import re


INPUT = os.getcwd() + '/programs/'
OUTPUT = os.getcwd() + '/exe/'
ERROR = os.getcwd() + '/error/'
codes = {}

'''
1. Writes new .c files with input size and nice value
2. Compiles and moves executables to separate folder
'''

def write(program_name, program_code, input_size, nice_value):
	global INPUT, OUTPUT

	new_path = (OUTPUT + program_name)
	if not os.path.exists(new_path):
		os.makedirs(new_path)

	try:
		new_code = program_code[:]
		
		''' Line numbers 9 and 10 in .c files '''
		new_code[8] = '#define INPUT_SIZE ' + str(input_size) + '\n'
		new_code[9] = '#define NICE_VALUE ' + str(nice_value) + '\n'

		allocation_method = random.randint(0,2)
		allocation_lines_1 = map(int, new_code[11].split('METHOD_1 ')[1].split(','))
		allocation_lines_2 = map(int, new_code[12].split('METHOD_2 ')[1].split(','))
		allocation_lines_3 = map(int, new_code[13].split('METHOD_3 ')[1].split(','))

		new_code[allocation_lines_1[0]-1], new_code[allocation_lines_1[1]-1] = '/*\n', '*/\n'
		new_code[allocation_lines_2[0]-1], new_code[allocation_lines_2[1]-1] = '/*\n', '*/\n'
		new_code[allocation_lines_3[0]-1], new_code[allocation_lines_3[1]-1] = '/*\n', '*/\n'
		new_code[allocation_lines_3[2]-1], new_code[allocation_lines_3[3]-1] = '/*\n', '*/\n'

		if allocation_method == 0:
			# Static variable
			new_code[allocation_lines_1[0]-1], new_code[allocation_lines_1[1]-1] = '\n', '\n'
		elif allocation_method == 1:
			# Non-static variable
			new_code[allocation_lines_2[0]-1], new_code[allocation_lines_2[1]-1] = '\n', '\n'
		else:
			# Pointer - Dynamic
			new_code[allocation_lines_3[0]-1], new_code[allocation_lines_3[1]-1] = '\n', '\n'
			new_code[allocation_lines_3[2]-1], new_code[allocation_lines_3[3]-1] = '\n', '\n'

		'''
		for _ in new_code:
			print _,
		raw_input()
		'''

		with open(INPUT + program_name + '.c', 'w') as w:
			w.writelines(new_code)
		
		''' 2 '''
		command = 'gcc %s -o %s/%s_%s_%s' % (INPUT + program_name + '.c', new_path, program_name.split('.')[0], input_size, nice_value)
		#print command
		
		if Popen(command, stdout=PIPE, stderr = PIPE, shell = True).communicate()[1] != '':
			raise Exception('Error in gcc')			

	except Exception as e:
		print(e)
		shutil.rmtree(new_path)
		with open(ERROR + 'error.txt', 'a') as f:
			f.write(str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S")) + '\t' + 'Compiling\tNew\t' + str(e) + '\n')


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
	
	with open('input.csv', 'r') as csvfile:
		rows = csv.reader(csvfile)
		i = 0
		for row in rows:
			''' Compile for each combination '''
			print(str(i) + '. Compiling ' + row[0].split('.')[0] + '_' + str(row[1]) + '_' + str(row[2]))
			write(row[0].split('.')[0], codes[row[0]], row[1], row[2])
			i += 1


if __name__ == "__main__":
	main()
