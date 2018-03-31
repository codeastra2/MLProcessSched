import csv
import os

INPUT_BATCH = os.getcwd().rpartition('/')[0] + '/batch_programs/csv'
INPUT_INDIVIDUAL = os.getcwd().rpartition('/')[0] + '/individual_programs/csv'

m = {}
keys=['id', '.bss', '.comment', '.data', '.dynamic', '.dynstr', '.dynsym', '.eh_frame', '.eh_frame_hdr', '.fini', '.fini_array', '.gnu.hash', '.gnu.version', '.gnu.version_r', '.got', '.init', '.init_array', '.input_size', '.interp', '.nice_value', '.note.ABI-tag', '.note.gnu.build-id', '.plt', '.plt.got', '.rela.dyn', '.rela.plt', '.rodata', '.shstrtab', '.strtab', '.symtab', '.text', 'start_time', 'end_time', 'total_time']

programs = ['bub', 'fib', 'mat', 'ms', 'hs', 'fac']
count = {}

for program in programs:
	m[program] = {}
	count[program] = 0

for key in keys:
	for program in programs:
		m[program][key]=[]

choice = int(raw_input('Enter 1 for batch, 2 for individual\n'))
choice = INPUT_BATCH if choice == 1 else INPUT_INDIVIDUAL

for file in os.listdir(choice):
	if len(file.split('.')) >1 and file.split('.')[1] == 'csv':
		f=open(choice+'/'+file)
		for line in f.readlines():
			line=line.split(',')
			if line[0] in programs:
				for i in range(1,len(line)):
					m[line[0]][keys[i]].append(int(float(line[i].strip())))
				count[line[0]] += 1


print(count)

with open(os.getcwd() + '/' + 'output_' + choice.split('_')[0].rpartition('/')[2] + '.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['program'] + programs)
	for key in keys[1:]:
		t = [key]
		for program in programs:
			t.append(len(set(m[program][key])))
		writer.writerow(t)
