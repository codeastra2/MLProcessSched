import pandas
import sys
from sklearn import model_selection, tree
from sklearn.externals import joblib

df = pandas.read_csv('nice_value_input_' + sys.argv[1] + '.csv')
array = df.values
X = array[:, 0:120]
Y = array[:, 120:124]
test_size = 0.33
seed = 7
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, Y_train)
Y_pred = clf.predict(X_test)
accu_count = 0
for idx, y_expected in enumerate(Y_test):
    y_actual = Y_pred[idx]
    #print(y_actual)
    #print(y_expected)
    #print('***********************')
    if y_actual.tolist() == y_expected.tolist():
        accu_count += 1
accu_per = accu_count*100/len(Y_test)
print("The accuracy per. is: " + str(accu_per))
filename = "model_nice_batch_" + sys.argv[1] + ".sav"
joblib.dump(clf, filename)