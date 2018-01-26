from sys import argv
from subprocess import Popen, PIPE
from os import listdir
import os.path, csv


dic={}
path = os.getcwd() + '/exe/'
dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]


'''
27 attributes
'''
def parse_1(s):
	global dic
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
def parse_2(s, input_size, nice_value):
	global dic
	lines = list(s)
	dic['.text'] = int(lines[1].split()[0])
	dic['.data'] = int(lines[1].split()[1])
	dic['.bss'] = int(lines[1].split()[2])
	dic['.input_size'] = int(input_size)
	dic['.nice_value'] = int(nice_value)


'''
Creates a line of text from sorted keys
'''
def create_line(file):
	global dic
	li = []
	keys = dic.keys()
	keys.sort()
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
for dir in dirs:
	dir = path + dir
	output_1 = []
	output_2 = []
	
	''' 1 and 2'''
	for file in os.listdir(dir):
		dic = {}
		input_size, nice_value = file.split('_')[1:]

		command = 'readelf -SW %s' % dir + '/' + file
		parse_1(Popen(command, shell=True, stdout=PIPE).stdout)
		
		command = 'size %s' % dir + '/' + file
		parse_2(Popen(command, shell=True, stdout=PIPE).stdout, input_size, nice_value)
		t = create_line(file)
		output_1.append(t)

	''' 3 '''
	command = ''
	for file in os.listdir(dir):
		command += './' + file + ' ' + str(file.split('_')[1]) + ' ' + str(file.split('_')[2]) + ' & '
	
	command += 'wait'
	output_2 = (Popen(command, stdout=PIPE, shell = True, cwd = dir).communicate()[0].strip()).splitlines()
	
	''' 4 '''
	for i in range(len(output_2)):
		output_2[i] = output_2[i].split(',')
	
	''' 5 '''
	with open('output.csv', 'a') as f:
	    w = csv.writer(f, dialect='excel')
	    for i in output_1:
	    	t = []
	    	for j in output_2:
	    		if i[0] == j[0]:
	    			t.append(int(j[1]))
	    			t.append(int(j[2]))
	    			t.append(int(j[3]))
	    	w.writerow(i + t)

	print 'Done with ' + dir