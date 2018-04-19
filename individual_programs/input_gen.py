import csv
import random

nice_values = range(-15,20)

m = {}
m['bub.c'] = [1000,10000]
m['fac.c'] = [500,5000]
m['fib.c'] = [29,35]
m['hs.c'] = [1000,100000]
m['mat.c'] = [100,340]
m['ms.c'] = [1000,100000]

# List the programs that need to be run individually
programs = ['bub.c', 'fac.c', 'mat.c', 'hs.c']

with open('input.csv', 'w') as f:
	w = csv.writer(f, dialect='excel')
	for program in programs:
		for i in range(500):
			w.writerow([program, random.randint(m[program][0], m[program][1]), random.choice(nice_values)])
