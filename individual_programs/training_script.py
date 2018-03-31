import pandas
from sklearn import model_selection, tree
from sklearn.metrics import accuracy_score

df = pandas.read_csv("dataset.csv")
array = df.values
X = array[:, 0:31]
for index in range(len(X)):
    X[index][0] = 1
Y = array[:, 33]
test_size = 0.33
seed = 7
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)
clf = tree.DecisionTreeRegressor(criterion="mae", splitter="random")
clf = clf.fit(X_train, Y_train)
error_percentage = ((abs(clf.predict(X_test) - Y_test)/(Y_test))*100)
print(sum(error_percentage)/len(error_percentage))