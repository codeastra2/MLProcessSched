from subprocess import Popen, PIPE
from os import listdir
import os.path, csv


INPUT = os.getcwd()+ '/exe/'
attributes = []
data = {}


'''
5 attributes
'''
def command_size(command, input_size, nice_value):
	global INPUT, attributes, data

	s = Popen(command, shell=True, stdout=PIPE).stdout
	lines = list(s)
	data['.text'] = int(lines[1].split()[0])
	data['.data'] = int(lines[1].split()[1])
	data['.bss'] = int(lines[1].split()[2])
	data['.input_size'] = int(input_size)
	data['.nice_value'] = int(nice_value)


'''
27 attributes
'''
def command_readelf(command):
	global INPUT, attributes, data

	s = Popen(command, shell=True, stdout=PIPE).stdout
	lines = list(s)
	count = int(lines[0].split(' ')[2])
	required_keys = ['.interp','.note.ABI-tag','.note.gnu.build-id', '.gnu.hash', '.dynsym', '.dynstr', '.gnu.version', '.gnu.version_r', '.rela.dyn', '.rela.plt', '.init', '.plt', '.plt.got','.fini', '.rodata', '.eh_frame_hdr', '.eh_frame', '.init_array', '.fini_array', '.jcr', '.dynamic', '.got', '.got.plt', '.comment', '.shstrtab', '.symtab', '.strtab']
	
	for i in range(1, count):
		line = lines[4+i].split()
		if i <= 9:
			if line[2] in required_keys:
				data[line[2]] = int(line[6], 16)
		else:
			if line[1] in required_keys:
				data[line[1]] = int(line[5], 16)


'''
Creates a line of text with keys in sorted order
'''
def create_csv_row(file):
	global INPUT, attributes, data
	li = []
	keys = data.keys()
	keys.sort()
	if not attributes:
		attributes = keys[:]
		attributes += ['start_time', 'end_time', 'total_time']
	
	for key in keys:
		li.append(data[key])
	li = [file.split('_')[0]] + li
	return li


'''
1. Collects attributes from readelf
2. Collects attributes from size
3. Runs the executables
4. Collects attributes post execution
5. Log to CSV
'''
def run_set(path):
	global INPUT, attributes, data

	run = ''
	output_1 = []
	output_2 = []
	
	''' 1 and 2'''
	for file in os.listdir(path):
		data = {}
		run += './' + file + ' & '
		command_readelf('readelf -SW %s' % path + file)
		command_size('size %s' % path + file, file.split('_')[1], file.split('_')[2])
		output_1.append(create_csv_row(file))

	''' 3 '''
	run += 'wait'
	output_2 = Popen(run, stdout=PIPE, shell = True, cwd = path).communicate()[0].strip().splitlines()
	
	''' 4 '''
	for i in range(len(output_2)):
		output_2[i] = output_2[i].split(',')
	
	''' 5 '''
	with open('output.csv', 'a') as f:
	    w = csv.writer(f, dialect='excel')
	    if os.stat('output.csv').st_size == 0:
	    	w.writerow(['id']+attributes)
	    for i in output_1:
	    	t = []
	    	for j in output_2:
	    		if i[0] == j[0]:
	    			t.append(int(j[1]))
	    			t.append(int(j[2]))
	    			t.append(int(j[3]))
	    	w.writerow(i + t)


def main():
	global INPUT, attributes, data

	directories = os.listdir(INPUT)
	directories.sort()
	for directory in directories:
		print('Running ' + directory)
		run_set(INPUT + directory + '/')


if __name__ == "__main__":
	main()
