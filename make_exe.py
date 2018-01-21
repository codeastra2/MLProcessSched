from sys import argv
def make_exe(filename, path):
	"""
	Compiles filename and makes executables in path
	"""
	from subprocess import Popen, PIPE
	f = open(filename, "r")
	linenum = 0
	lines = []
	flag = False
	for line in f:
		if "#define" in line:
			flag = True
		else:
			if flag == False:
				linenum += 1
		lines.append(line)

	for i in range(1, 46):
		temp_line = lines[linenum].split(" ")
		temp_line[-1] = str(i)+"\n"
		lines[linenum] = ' '.join(temp_line)
		f1 = open(filename, "w")
		f1.write(''.join(lines))
		f1.close()
		command = "gcc %s -o %s%s%d" % (filename, path, filename.split(".")[0], i)
		Popen(command, shell=True, stdout=PIPE).stdout

make_exe(argv[1], argv[2])