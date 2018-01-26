from subprocess import Popen, PIPE
import csv, glob, os


src_path = os.getcwd()+ '/programs/'
dest_path = os.getcwd() + '/exe/'
files = glob.glob(src_path + '*.c')

if not os.path.exists(dest_path):
	os.makedirs(dest_path)


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
			exe_folder = dest_path + str(i) + '/'
			if not os.path.exists(exe_folder):
				os.makedirs(exe_folder)
			compile(values, exe_folder)
			i = i+1


'''
Name compiled file with input size and executable
'''	
def compile(values, exe_folder):
	for file in files:
		name = os.path.basename(file)
		command = 'gcc %s -o %s/%s_%d_%d' % (name, exe_folder , name.split('.')[0], values[name][0], values[name][1])
		#print command
		Popen(command, shell=True, stdout=PIPE, cwd = src_path).stdout


'''
Start of program
'''
read()
