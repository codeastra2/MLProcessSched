# To pick only rows having nice value greater than certain value
import csv
import random

first = True
max_instances = 0
neg = 0

with open('dataset_full.csv', 'r') as csvfile:
	rows = csv.reader(csvfile)
	with open('transform.csv', 'w') as f:
		writer = csv.writer(f)
		for row in rows:
			if first:
				first = False
				writer.writerow(row)
				continue
			if int(row[19]) > 0:
				writer.writerow(row)
			elif neg < 100 and random.randint(1,20) > 10:   # Bias = 5 out of 100
				neg += 1
				if int(row[19]) < -15:
					row[19] = int(row[19]) + 5
				writer.writerow(row)
			max_instances += 1

print('Total rows = ' + str(max_instances))
print('Negative = ' + str(neg))
