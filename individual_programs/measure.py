from sklearn.externals import joblib

import sys
import pandas
import csv
import os
import matplotlib.pyplot as plt
 

df = pandas.read_csv('measure_' + sys.argv[1] + '.csv')
array = df.values
Y = array[:, 33]

better_count = 0
better_time = []
better_ratio = 0

time_custom_nice_total = []
time_zero_nice_total = []

time_custom_nice_better = []
time_zero_nice_better = []

time_custom_nice_worse = []
time_zero_nice_worse = []


def count():
	global better_count, better_time, better_ratio, time_custom_nice_total, time_zero_nice_total, time_custom_nice_better, time_zero_nice_better, time_custom_nice_worse, time_zero_nice_worse
	for index in range(0, len(Y), 2):
	    if index + 1 < len(Y):
	        if (Y[index+1] - Y[index]) > 0:
	            better_count += 1
	            better_time.append(Y[index+1] - Y[index])
	            time_custom_nice_better.append(Y[index])
	            time_zero_nice_better.append(Y[index+1])
	        else:
	        	time_custom_nice_worse.append(Y[index])
	        	time_zero_nice_worse.append(Y[index+1])
	        
	        time_custom_nice_total.append(Y[index])
	        time_zero_nice_total.append(Y[index+1])

	better_ratio = 2.0 * better_count/len(Y)
	print(better_count, len(Y))
	print(better_ratio * 100)
	print((1.0 * sum(time_custom_nice_total)/sum(time_zero_nice_total)))

	write_results()
	plots()


def write_results():
	li1 = [sum(time_zero_nice_total), sum(time_custom_nice_total), sum(time_zero_nice_total) - sum(time_custom_nice_total), (sum(time_zero_nice_total) - sum(time_custom_nice_total))/len(time_zero_nice_total), (1.0 * sum(time_custom_nice_total)/sum(time_zero_nice_total))]
	li2 = [sum(time_zero_nice_better), sum(time_custom_nice_better), sum(time_zero_nice_better) - sum(time_custom_nice_better), (sum(time_zero_nice_better) - sum(time_custom_nice_better))/len(time_zero_nice_better), (1.0 * sum(time_custom_nice_better)/sum(time_zero_nice_better))]
	li3 = [sum(time_zero_nice_worse), sum(time_custom_nice_worse), sum(time_zero_nice_worse) - sum(time_custom_nice_worse), (sum(time_zero_nice_worse) - sum(time_custom_nice_worse))/len(time_zero_nice_worse), (1.0 * sum(time_custom_nice_worse)/sum(time_zero_nice_worse))]

	with open('results.csv', 'a') as f:
		w = csv.writer(f, dialect='excel')
		if os.stat('results.csv').st_size == 0:
			w.writerow(['model','case', 'Time for 0 nice value', 'Time for custom nice value', 'Time saved', 'Time saved per program', 'Ratio of custom and 0 nice'])
		w.writerow([sys.argv[1], 'total'] + li1)
		w.writerow([sys.argv[1], 'better'] + li2)
		w.writerow([sys.argv[1], 'worse'] + li3)

	'''
	print('TOTAL\n')
	print('Time for 0 nice = ' + str(sum(time_zero_nice_total)))
	print('Time for custom nice = ' + str(sum(time_custom_nice_total)))
	print('Time saved = ' + str(sum(time_zero_nice_total) - sum(time_custom_nice_total)))
	print('Time saved per program = ' + str( (sum(time_zero_nice_total) - sum(time_custom_nice_total))/len(time_zero_nice_total)) )
	print('Ratio of custom and 0 nice = ' + str(1.0 * sum(time_custom_nice_total)/sum(time_zero_nice_total)))
	print('\n\n\n')
	'''


def plots():
	len_list = [point for point in range(1, len(better_time)+1)]
	plt.scatter(len_list, better_time, s=4)
	 
	plt.title('Scatter plot for showing how better out program is compared to default')
	plt.xlabel('Succes ratio = %s percent)' % better_ratio * 100)
	plt.ylabel('Better time (in microseconds)')
	plt.show()


count()
