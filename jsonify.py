from sys import argv
def parse(path):
	def jsonify(string):
		lines = []
		for line in string:
			lines.append(line)
		count = int(lines[0].split(" ")[2])
		attr = {}
		required_keys = [".gnu.hash", ".dynamic", ".dynsym", ".dynstr", ".got",
		".plt", ".rodata", ".rela.dyn"]
		for i in range(1, count):
			split_line = lines[4+i].split()
			if i <= 9:
				if split_line[2] in required_keys:
					attr[split_line[2]] = int(split_line[6], 16)
			else:
				if split_line[1] in required_keys:
					attr[split_line[1]] = int(split_line[5], 16)
		return attr

	from os import listdir
	from subprocess import Popen, PIPE
	from json import dump
	files = listdir(path)
	data = {}
	digits = [str(i) for i in range(10)]
	for filename in files:
		command = "readelf -SW %s" % path+filename
		print filename
		ind = 0
		while filename[ind] not in digits:
			ind += 1
		input_size = int(filename[ind:])

		temp_data = jsonify(Popen(command, shell=True, stdout=PIPE).stdout)
		command = "size %s" % path+filename
		size_data = Popen(command, shell=True, stdout=PIPE).stdout
		lines = []
		for line in size_data:
			lines.append(line)

		temp_data["text"] = int(lines[1].split()[0])
		temp_data["data"] = int(lines[1].split()[1])
		temp_data["bss"] = int(lines[1].split()[2])
		temp_data["input_size"] = input_size
		data[filename] = temp_data

	dump(data, open("data.json", "w"))


parse(argv[1])