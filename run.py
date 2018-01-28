from subprocess import Popen, PIPE
from os import listdir
import os.path, csv


PATH = os.getcwd() + '/exe/'
dic = {}
row_header = []


'''
27 attributes
'''
def command_readelf(command):
	global dic
	s = Popen(command, shell=True, stdout=PIPE).stdout
	lines = list(s)
	count = int(lines[0].split(' ')[2])
	required_keys = ['.interp','.note.ABI-tag','.note.gnu.build-id', '.gnu.hash', '.dynsym', '.dynstr', '.gnu.version', '.gnu.version_r', '.rela.dyn', '.rela.plt', '.init', '.plt', '.plt.got','.fini', '.rodata', '.eh_frame_hdr', '.eh_frame', '.init_array', '.fini_array', '.jcr', '.dynamic', '.got', '.got.plt', '.comment', '.shstrtab', '.symtab', '.strtab']
	
	for i in range(1, count):
		line = lines[4+i].split()
		if i <= 9:
			if line[2] in required_keys:
				dic[line[2]] = int(line[6], 16)
		else:
			if line[1] in required_keys:
				dic[line[1]] = int(line[5], 16)


'''
5 attributes
'''
def command_size(command, input_size, nice_value):
	global dic
	s = Popen(command, shell=True, stdout=PIPE).stdout
	lines = list(s)

	dic['.text'] = int(lines[1].split()[0])
	dic['.data'] = int(lines[1].split()[1])
	dic['.bss'] = int(lines[1].split()[2])
	dic['.input_size'] = int(input_size)
	dic['.nice_value'] = int(nice_value)


'''
Creates a line of text from sorted keys
'''
def create_csv_row(file):
	global dic
	global row_header
	li = []
	keys = dic.keys()
	keys.sort()
	if not row_header:
		row_header = keys[:]
		row_header += ['start_time', 'end_time', 'total_time']
	
	for key in keys:
		li.append(dic[key])
	li = [file.split('_')[0]] + li
	return li


'''
1. Collects attributes from readelf
2. Collects attributes from size
3. Runs the executables
4. Collects attributes post execution
5. Log to CSV
'''
def run_set(values):
	global PATH
	run = ''
	output_1 = []
	output_2 = []
	
	''' 1 and 2'''
	for file in os.listdir(PATH):
		dic = {}
		run += './' + file + ' ' + str(values[file][0]) + ' ' + str(values[file][1]) + ' & '
		command_readelf('readelf -SW %s' % PATH + file)
		command_size('size %s' % PATH + file, values[file][0], values[file][1])
		output_1.append(create_csv_row(file))

	''' 3 '''
	run += 'wait'
	output_2 = Popen(run, stdout=PIPE, shell = True, cwd = PATH).communicate()[0].strip().splitlines()
	
	''' 4 '''
	for i in range(len(output_2)):
		output_2[i] = output_2[i].split(',')
	
	''' 5 '''
	with open('output.csv', 'a') as f:
	    w = csv.writer(f, dialect='excel')
	    if os.stat('output.csv').st_size == 0:
	    	w.writerow(['id']+row_header)
	    for i in output_1:
	    	t = []
	    	for j in output_2:
	    		if i[0] == j[0]:
	    			t.append(int(j[1]))
	    			t.append(int(j[2]))
	    			t.append(int(j[3]))
	    	w.writerow(i + t)


'''
Read input sizes and nice values for a batch of programs from CSV
'''
def read():
	i = 1
	with open('input.csv', 'r') as csvfile:
		rows = csv.reader(csvfile)
		for row in rows:
			print ('Set ' + row[0])
			del row[0]
			values = {}
			values[row[0]] = [int(row[1]), int(row[2])]
			values[row[3]] = [int(row[4]), int(row[5])]
			values[row[6]] = [int(row[7]), int(row[8])]
			values[row[9]] = [int(row[10]), int(row[11])]
			values[row[12]] = [int(row[13]), int(row[14])]
			run_set(values)
			i = i + 1

read()
