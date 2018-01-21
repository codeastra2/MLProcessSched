import inspect, os, glob, random, subprocess


def getNice():
	#Code has to be written to generate all combinations of nice values. Returning random values for now.
	return random.randint(-20,19)


def getInputSize(s):
	ans = ""
	for char in s:
		if(char.isdigit()):
			ans += char
	return ans


def getCommand():
	current_directory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) 
	files = glob.glob(current_directory + "/*")
	command = ""

	for file in files:
		name = os.path.basename(file)
		if name != "dataset_gen.py":
			command += "./" + name + " " + str(getInputSize(name)) + " " + str(getNice()) + " & "

	command += "wait"
	return command

process = subprocess.Popen(getCommand() , stdout=subprocess.PIPE, shell = True)
proc_stdout = process.communicate()[0].strip()
print proc_stdout
