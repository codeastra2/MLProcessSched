# To pick only rows having certain nice value
import csv
import random

neg = 0
modified = 0
unmodified = 0
max_instances = 800													#Bias of number of rows needed = 4 * number of sets of parallel programs
instances = 0
scanned = 0
c = 0

lines = []

with open('dataset_full.csv', 'r') as csvfile:
	rows = list(csv.reader(csvfile))
	header = rows[0]
	del rows[0]
	print(len(rows))
	for i in range(len(rows)):
		if instances <= max_instances:
			scanned += 1
			if i%4 == 0 and i+4 < len(rows):
				flag = random.choice([True] + [False] * 500)		#Bias of picking a set of parallel programs
				if flag:
					instances += 4
			if flag:
				c += 1
				if int(rows[i][19]) > 0:
					unmodified += 1
					lines.append(rows[i])
				elif neg < 10000 and random.randint(1,20) > 15:   	#Bias of negative values = 5 out of 100
					neg += 1
					if int(rows[i][19]) < -15:
						rows[i][19] = int(rows[i][19]) + 5
					lines.append(rows[i])
				else:
					modified += 1
					if int(rows[i][19]) < 0:
						rows[i][19] = int(rows[i][19]) * -1
					lines.append(rows[i])

lines = lines[:len(lines)-1]
print(len(lines))

with open('transform.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(header)
	for line in lines:
		writer.writerow(line)

print('Total rows = ' + str(max_instances))
print('Negative = ' + str(neg))
print('Modified = ' + str(modified))
print('Unmodified = ' + str(unmodified))
print('Scanned rows = ' + str(scanned))