from sklearn import preprocessing
from sklearn.feature_selection import VarianceThreshold
from sklearn.model_selection import GridSearchCV
from sklearn.externals import joblib

from sklearn import model_selection, tree
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.neural_network import MLPClassifier, MLPRegressor

from sklearn.metrics import r2_score
from sklearn.metrics import explained_variance_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

import sys
import numpy as np
import pandas
import graphviz
import scikitplot
import matplotlib.pyplot as plt

prog_map = {"bub":"1", "fac":"2", "mat":"3", "hs":"4", "fib":"5", "ms":"6"}
Y_test = []
prediction = []

df = pandas.read_csv("dataset.csv")
array = df.values
columns = df.columns
X = array[:, 0:31]
Y = array[:, 33]

for index in range(len(X)):
    X[index][0] = prog_map[X[index][0]]

selection = VarianceThreshold()
X = selection.fit_transform(X)

temp_list = []
selected_columns = selection.get_support()
for i in range(len(selected_columns)):
	if selected_columns[i]:
		temp_list.append(columns[i])

selected_columns = temp_list


'''
Decision Tree - C4.5
'''

def dt():
	global Y_test, prediction
	
	test_size = 0.30
	X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size = test_size)

	model = tree.DecisionTreeRegressor(criterion = 'mse', splitter = 'best')
	model.fit(X_train, Y_train)

	prediction = model.predict(X_test)
	print_accuracy(model, 'model_dt')

	scikitplot.estimators.plot_feature_importances(model, feature_names=selected_columns, x_tick_rotation = 90, order = None, text_fontsize='small')
	plt.title('')
	plt.ylabel('Feature Importance')
	plt.show()

	
	#graphviz.Source(tree.export_graphviz(model,out_file=None,feature_names=selected_columns,filled=True,rounded=True,special_characters=True)).render('dt.png')


'''
Decision Tree with ADA Boost
'''

def dtb():
	global Y_test, prediction

	test_size = 0.30
	X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size)

	model = AdaBoostRegressor(DecisionTreeRegressor(max_depth=50), n_estimators=25, loss = 'exponential')
	model.fit(X_train, Y_train)

	prediction = model.predict(X_test)
	print_accuracy(model, 'model_dtb')

	plt.plot(range(len(prediction)), prediction, 'ro')
	plt.plot(range(len(prediction)), Y_test)
	plt.legend(['Prediction', 'Actual data'], loc = 'best')
	plt.title('')
	plt.xlabel('Testing data')
	plt.ylabel('Time in microseconds')
	plt.show()



'''
Random Forest
'''

def rf():
	global Y_test, prediction

	test_size = 0.30
	X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size)

	model = RandomForestRegressor(criterion = 'mse', n_estimators = 10)
	clf = model.fit(X_train, Y_train)

	prediction = model.predict(X_test)
	print_accuracy(model, 'model_rf')
	
	scikitplot.estimators.plot_learning_curve(model, X_test, Y_test)
	plt.title('Learning Curve')
	plt.show()


'''
k Nearest Neighbour
'''

def knn():
	global Y_test, prediction

	test_size = 0.40
	X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=1)

	parameters = {'n_neighbors':[2, 5, 10], 'weights':['uniform', 'distance'], 'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute']}

	#model = KNeighborsRegressor(n_neighbors = 2, algorithm='auto', weights='distance')
	model = KNeighborsRegressor()
	model = GridSearchCV(model, parameters, verbose = 1)
	model.fit(X_train, Y_train)

	prediction = model.predict(X_test)
	print_accuracy(model, 'model_knn')

	plt.hist(Y_test, bins = 100, histtype = 'stepfilled')
	plt.xlabel('Testing data')
	plt.ylabel('Time in microseconds')
	plt.show()
	

'''
Support Vector Machine
'''

def svm():
	global Y_test, prediction
	
	test_size = 0.20
	X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=1)
	
	# This scales to negative values also. Hence some values in print_accuracy() may not be right.
	X_train =  preprocessing.scale(X_train)
	X_test = preprocessing.scale(X_test)
	Y_train = preprocessing.scale(Y_train)
	Y_test = preprocessing.scale(Y_test)

	parameters = {'kernel':('linear', 'poly', 'rbf', 'sigmoid'), 'C':[1, 10], 'shrinking': (True, False)}
	
	#model = svm.SVR(C=1000, epsilon=0.1, kernel = 'rbf')
	model = SVR()
	model = GridSearchCV(model, parameters, verbose = 1)
	model.fit(X_train, Y_train)
	
	prediction = model.predict(X_test)
	print_accuracy(model, 'model_svm')


'''
Multi Layer Perceptron
'''

def mlp():
	global Y_test, prediction
	
	test_size = 0.30
	X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=1)
	
	# This scales to negative values also. Hence some values in print_accuracy() may not be right.
	X_train =  preprocessing.scale(X_train)
	X_test = preprocessing.scale(X_test)
	Y_train = preprocessing.scale(Y_train)
	Y_test = preprocessing.scale(Y_test)
	
	param_grid = [{'activation' : ['identity', 'logistic', 'tanh', 'relu'], 'solver' : ['lbfgs', 'sgd', 'adam'], 'hidden_layer_sizes': [(1,),(5,),(10,),(15,),(20,),(30,),(50,)]}]
	
	model = MLPRegressor()
	model = GridSearchCV(model, param_grid, verbose = 1)
	model.fit(X_train, Y_train)

	prediction = model.predict(X_test)
	print_accuracy(model, 'model_mlp')


'''
Accuracy and error statistics
'''

def print_accuracy(model, name):
	difference = []
	for i in range(len(prediction)):
		difference.append( abs(prediction[i] - Y_test[i])/Y_test[i] )

	print('Raw Accuracy = ' + str(100.0 - (100 * sum(difference)/len(difference))))
	print('R2 Score = ' + str(r2_score(Y_test, prediction)))
	print('Explained Variance = ' + str(explained_variance_score(Y_test, prediction)))
	print('MAE = ' + str(mean_absolute_error(Y_test, prediction)))
	print('MSE = ' + str(mean_squared_error(Y_test, prediction)))
	joblib.dump(model, name + '.sav')


try:
	def undefined():
		print('No ML algorithm called ' + sys.argv[1])

	{
		'dt' : dt,
		'dtb': dtb,
		'rf' : rf,
		'knn': knn,
		'svm': svm,
		'mlp': mlp,
	}.get(sys.argv[1], undefined)()

except IndexError:
	print('No input model')
