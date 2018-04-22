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
	li1 = [sum(time_zero_nice_total), sum(time_custom_nice_total), sum(time_zero_nice_total) - sum(time_custom_nice_total), (sum(time_zero_nice_total) - sum(time_custom_nice_total))/len(time_zero_nice_total), (better_ratio * 100), (1.0 * sum(time_custom_nice_total)/sum(time_zero_nice_total))]
	li2 = [sum(time_zero_nice_better), sum(time_custom_nice_better), sum(time_zero_nice_better) - sum(time_custom_nice_better), (sum(time_zero_nice_better) - sum(time_custom_nice_better))/len(time_zero_nice_better), (better_ratio * 100), (1.0 * sum(time_custom_nice_better)/sum(time_zero_nice_better))]
	li3 = [sum(time_zero_nice_worse), sum(time_custom_nice_worse), sum(time_zero_nice_worse) - sum(time_custom_nice_worse), (sum(time_zero_nice_worse) - sum(time_custom_nice_worse))/len(time_zero_nice_worse), (better_ratio * 100), (1.0 * sum(time_custom_nice_worse)/sum(time_zero_nice_worse))]

	with open('results.csv', 'a') as f:
		w = csv.writer(f, dialect='excel')
		if os.stat('results.csv').st_size == 0:
			w.writerow(['model','case', 'Time for 0 nice value', 'Time for custom nice value', 'Time saved', 'Time saved per program', 'Percentage of programs better', 'Ratio of custom and 0 nice'])
		w.writerow([sys.argv[1], 'total'] + li1)
		w.writerow([sys.argv[1], 'better'] + li2)
		w.writerow([sys.argv[1], 'worse'] + li3)


def plots():
	len_list = [point for point in range(1, len(better_time)+1)]
	 
	#plt.hist([max(a-b,0) for a,b in zip(time_zero_nice_total, time_custom_nice_total)], bins = 100, histtype = 'stepfilled', color='g')
	#plt.bar(range(len(time_custom_nice_total)), [a-b for a,b in zip(time_zero_nice_total, time_custom_nice_total)], color='g')
	plt.title('Scatter plot for showing time saved by custom nice value')
	plt.xlabel('Testing data instances')
	plt.ylabel('Time saved (in microseconds)')
	#plt.show()
	
	plt.subplot(211)
	plt.plot(range(len(time_custom_nice_total[0:100])), time_custom_nice_total[0:100])
	plt.plot(range(len(time_zero_nice_total[0:100])), time_zero_nice_total[0:100])
	plt.title('Turn around time comparison ')
	plt.ylabel('Time (in microseconds)')
	plt.legend(['Custom nice value', 'Zero nice value'], loc = 'upper left')

	plt.subplot(212)
	plt.plot(range(len(time_custom_nice_total[100:200])), time_custom_nice_total[100:200])
	plt.plot(range(len(time_zero_nice_total[100:200])), time_zero_nice_total[100:200])
	plt.xlabel('Testing data instances')
	plt.ylabel('Time (in microseconds)')
	plt.legend(['Custom nice value', 'Zero nice value'], loc = 'upper left')

	plt.show()
	

count()
