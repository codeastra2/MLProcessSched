# To pick only rows having nice value greater than 0
import csv

first = True

with open('dataset.csv', 'r') as csvfile:
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