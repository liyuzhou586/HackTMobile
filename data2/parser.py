import numpy as np
import csv
import os
from sklearn.externals import joblib
from sklearn.tree import DecisionTreeClassifier as dt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier as ANN
from sklearn.metrics import classification_report
from sklearn.model_selection import validation_curve, StratifiedKFold, GridSearchCV

# Load data
if not os.path.exists('data2.npy'):
    print("Loading from csv")
    data2 = np.genfromtxt('data2.csv', dtype=None,
        delimiter=',', names=True, filling_values=0.0)
    np.save('data2.npy', data2)
else:
    print("Loading from .npy")
    data2 = np.load('data2.npy')

# Column names
header = data2.dtype.names

y = data2['Churn']
x = np.zeros((len(y), len(header) - 1))

if not os.path.exists('x.npy'):
    print("Converting")
# if True:
    ind = 0
    for i, h in enumerate(header):
        if h != 'Churn':
            raw = data2[h]
            # Make sure everyone is of type float
            if raw.dtype == np.int32:
                dat = raw.astype(np.float64)
            elif raw.dtype == np.float64:
                dat = raw
            else:
                dat = np.zeros(raw.shape)
                vals = np.unique(raw)
                for j, u in enumerate(vals):
                    dat[raw == u] = j
            if (np.isnan(dat).any()):
                print(dat)
                print(h)
            x[:,ind] = dat
            ind += 1
    for index, label in enumerate(y):
        if label.decode('UTF-8') == 'No':
            y[index] = 0
        else:
            y[index] = 1
    np.save('x.npy', x)
    np.save('y.npy', y)
else:
    print('Loading from x.npy, y.npy')
    x = np.load('x.npy')
    y = np.load('y.npy')


# Training
# Split into test/train
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# clf = dt(max_depth=10)
# print("Starting decision tree training...")
# clf = clf.fit(x_train, y_train)
# print("DT result: ", clf.score(x_test, y_test))
# target_names = ['Not Churn', 'Churn']
# y_pred = clf.predict(x_test)
# print(classification_report(y_test, y_pred, target_names=target_names))

# print("Starting SVM training...")
# clf = SVC(C=1, kernel='rbf', gamma=0.125,
#             decision_function_shape='ovr')
# clf = clf.fit(x_train, y_train)
# print("SVM result: ", clf.score(x_test, y_test))
# target_names = ['Not Churn', 'Churn']
# y_pred = clf.predict(x_test)
# print(classification_report(y_test, y_pred, target_names=target_names))

print("Starting ANN training...")

# alphas = [10 ** -x for x in np.arange(-1, 9.01, 1)]
# layer_range = [(h,) * l for l in [1, 2, 3] for h in range(15, 35, 5)]
# learning_range = sorted([(2**x)/1000 for x in range(8)]+[0.000001])
# param_dists = {"hidden_layer_sizes": layer_range,
#     'learning_rate_init': learning_range,
#     'alpha': alphas
#     }

# # Parameters for Grid Search Cross Validation
# clf = ANN(activation='relu', solver="adam", max_iter=5000)
# cv = StratifiedKFold(n_splits=5, shuffle=True)
# grid_search = GridSearchCV(clf, param_grid=param_dists,
#     scoring="balanced_accuracy", cv=cv, refit=True, n_jobs=-1)
# grid_search.fit(x, y)

# # Best hyperparameters and estimator with the best hyperparameters
# best_nn = grid_search.best_estimator_
# best_params = grid_search.best_params_
# best_cv_score = grid_search.best_score_
# print("optimal parameters: " + str(best_params))
# print("Cross validation accuracy: " + str(best_cv_score))


best_params1 = { 'hidden_layer_sizes': (25, 25, 25),
                'alpha': 0.001,
                'learning_rate_init': 0.004
                }

best_params2 = { 'hidden_layer_sizes': (30, 30),
                'alpha': 1e-9,
                'learning_rate_init': 0.008
                }

best_params3 = { 'hidden_layer_sizes': (20, ),
                'alpha': 0.1,
                'learning_rate_init': 0.032
                }

best_params4 = { 'hidden_layer_sizes': (25, ),
                'alpha': 1e-8,
                'learning_rate_init': 0.032
                }

# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
# clf = ANN(hidden_layer_sizes=best_params1['hidden_layer_sizes'],
#                  activation="relu",
#                  solver='adam',
#                  alpha=best_params1['alpha'],
#                  learning_rate="constant",
#                  learning_rate_init=best_params1['learning_rate_init'],
#                  max_iter=10000)
# clf = clf.fit(x_train, y_train)
# print("ANN1 result: ", clf.score(x_test, y_test))
# target_names = ['Not Churn', 'Churn']
# y_pred = clf.predict(x_test)
# print(classification_report(y_test, y_pred, target_names=target_names))

# clf = ANN(hidden_layer_sizes=best_params2['hidden_layer_sizes'],
#                  activation="relu",
#                  solver='adam',
#                  alpha=best_params2['alpha'],
#                  learning_rate="constant",
#                  learning_rate_init=best_params2['learning_rate_init'],
#                  max_iter=10000)
# clf = clf.fit(x_train, y_train)
# print("ANN2 result: ", clf.score(x_test, y_test))
# target_names = ['Not Churn', 'Churn']
# y_pred = clf.predict(x_test)
# print(classification_report(y_test, y_pred, target_names=target_names))

# clf = ANN(hidden_layer_sizes=best_params3['hidden_layer_sizes'],
#                  activation="relu",
#                  solver='adam',
#                  alpha=best_params3['alpha'],
#                  learning_rate="constant",
#                  learning_rate_init=best_params3['learning_rate_init'],
#                  max_iter=10000)
# clf = clf.fit(x_train, y_train)
# print("ANN3 result: ", clf.score(x_test, y_test))
# target_names = ['Not Churn', 'Churn']
# y_pred = clf.predict(x_test)
# print(classification_report(y_test, y_pred, target_names=target_names))

# clf = ANN(hidden_layer_sizes=best_params4['hidden_layer_sizes'],
#                  activation="relu",
#                  solver='adam',
#                  alpha=best_params4['alpha'],
#                  learning_rate="constant",
#                  learning_rate_init=best_params4['learning_rate_init'],
#                  max_iter=10000)
# clf = clf.fit(x_train, y_train)
# print("ANN4 result: ", clf.score(x_test, y_test))
# target_names = ['Not Churn', 'Churn']
# y_pred = clf.predict(x_test)
# print(classification_report(y_test, y_pred, target_names=target_names))

clf = ANN(hidden_layer_sizes=best_params3['hidden_layer_sizes'],
                 activation="relu",
                 solver='adam',
                 alpha=best_params3['alpha'],
                 learning_rate="constant",
                 learning_rate_init=best_params3['learning_rate_init'],
                 max_iter=10000)
clf = clf.fit(x, y)
print("ANN result: ", clf.score(x, y))
target_names = ['Not Churn', 'Churn']
y_pred = clf.predict(x)
print(classification_report(y, y_pred, target_names=target_names))
joblib.dump(clf, 'ANN.joblib')