from sklearn import model_selection, tree
from sklearn.externals import joblib

import pandas
import sys

df = pandas.read_csv('nice_value_input_' + sys.argv[1] + '.csv')
array = df.values
X = array[:, 0:120]
Y = array[:, 120:124]
test_size = 0.20

X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=1)
model = tree.DecisionTreeClassifier()
model = model.fit(X_train, Y_train)
prediction = model.predict(X_test)

accu_count = 0
for idx, y_expected in enumerate(Y_test):
    y_actual = prediction[idx]
    if y_actual.tolist() == y_expected.tolist():
        accu_count += 1

print("The accuracy percentage is: " + str(accu_count*100/len(Y_test)))
filename = "model_nice_batch_" + sys.argv[1] + ".sav"
joblib.dump(model, filename)
