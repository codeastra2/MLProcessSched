from sklearn.externals import joblib

import sys
import pandas
import matplotlib.pyplot as plt
 
df = pandas.read_csv('measure_' + sys.argv[1] + '.csv')
array = df.values
Y = array[:, 33]

better_count = 0
better_time = []

for index in range(0, len(Y), 2):
    if index + 1 < len(Y):
        if (Y[index+1] - Y[index]) > 0:
            better_count += 1
            better_time.append(Y[index+1] - Y[index])

better_ratio = 2.0 * better_count/len(Y)

print(better_count, len(Y))
print(better_ratio * 100)
print(sum(better_time)/len(better_time))
 
len_list = [point for point in range(1, len(better_time)+1)]
plt.scatter(len_list, better_time, s=4)
 
plt.title('Scatter plot for showing how better out program is compared to default')
plt.xlabel('Succes ratio = %s percent)' % better_ratio * 100)
plt.ylabel('Better time (in microseconds)')
plt.show()