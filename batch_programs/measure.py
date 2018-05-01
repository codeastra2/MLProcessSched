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

time_custom_nice_all = []
time_zero_nice_all = []

time_custom_nice_better = []
time_zero_nice_better = []

time_custom_nice_worse = []
time_zero_nice_worse = []


def count():
	global better_count, better_time, better_ratio, time_custom_nice_all, time_zero_nice_all, time_custom_nice_better, time_zero_nice_better, time_custom_nice_worse, time_zero_nice_worse
	for index in range(0, len(Y), 8):
		if index + 8 < len(Y):
			time_sum_custom = Y[index] + Y[index+1] + Y[index+2] + Y[index+3]
			time_sum_zero = Y[index+4] + Y[index+5] + Y[index+6] + Y[index+7]
			time_custom_nice_all.append(time_sum_custom)
	        time_zero_nice_all.append(time_sum_zero)

	        if time_sum_zero >= time_sum_custom:
				better_count += 1
				better_time.append(time_sum_zero - time_sum_custom)
				time_custom_nice_better.append(time_sum_custom)
				time_zero_nice_better.append(time_sum_zero)
	        else:
				time_custom_nice_worse.append(time_sum_custom)
				time_zero_nice_worse.append(time_sum_zero)

	#print(len(time_custom_nice_better), len(time_custom_nice_worse), len(time_custom_nice_all))
	if len(time_custom_nice_all) - len(time_custom_nice_better) - len(time_custom_nice_worse) > 0 :
		print(len(time_custom_nice_better), len(time_custom_nice_worse), len(time_custom_nice_all))
		raw_input('Lengths not matching')

	better_ratio = 1.0 * better_count/len(time_custom_nice_all)
	print(better_count, len(time_custom_nice_all))
	print(better_ratio * 100)
	print((1.0 * sum(time_custom_nice_all)/sum(time_zero_nice_all)))

	write_results()
	plots()


def write_results():
	li1 = [sum(time_zero_nice_all), sum(time_custom_nice_all), sum(time_zero_nice_all) - sum(time_custom_nice_all), (sum(time_zero_nice_all) - sum(time_custom_nice_all))/len(time_zero_nice_all), (better_ratio * 100), (1.0 * sum(time_custom_nice_all)/sum(time_zero_nice_all))]
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
	
	#plt.hist([max(a-b,0) for a,b in zip(time_zero_nice_all, time_custom_nice_all)], bins = 100, histtype = 'stepfilled', color='g')
	plt.bar(range(len(time_custom_nice_all)), [a-b for a,b in zip(time_zero_nice_all, time_custom_nice_all)], color='g')
	plt.title('Scatter plot for showing time saved by custom nice value')
	plt.xlabel('Testing data instances')
	plt.ylabel('Time saved (in microseconds)')
	plt.show()
	
	plt.subplot(211)
	plt.plot(range(len(time_custom_nice_all[0:100])), time_custom_nice_all[0:100])
	plt.plot(range(len(time_zero_nice_all[0:100])), time_zero_nice_all[0:100])
	plt.title('Turn around time comparison ')
	plt.ylabel('Time (in microseconds)')
	plt.legend(['Custom nice value', 'Zero nice value'], loc = 'upper left')

	plt.subplot(212)
	plt.plot(range(len(time_custom_nice_all[100:200])), time_custom_nice_all[100:200])
	plt.plot(range(len(time_zero_nice_all[100:200])), time_zero_nice_all[100:200])
	plt.xlabel('Testing data instances')
	plt.ylabel('Time (in microseconds)')
	plt.legend(['Custom nice value', 'Zero nice value'], loc = 'upper left')

	plt.show()
	step = len(time_zero_nice_all) / 20
	for i in range(0, len(time_zero_nice_all), step):
		if i + step < len(time_zero_nice_all):
			print('Testing set '+str(i)+' to '+str(i+step)+ ': ' +str(1.0*sum(time_custom_nice_all[i:i+step])/sum(time_zero_nice_all[i:i+step])))


count()
