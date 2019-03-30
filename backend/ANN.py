from sklearn.externals import joblib
import json
import numpy as np

clf = joblib.load('ANN.joblib')
data2 = np.load('data2.npy')
header = data2.dtype.names

def predict(json_input):
    print(json_input)
    table = json_input
    count = 0
    data = []
    for row in table:
        if count == 0:
            header = row.keys()
            count += 1
        data.append(list(row.values()))
    data_new = np.array(data)
    data_new.dtype = [(label, data_new.dtype) for label in header]

    x = np.zeros((len(table), len(header)))

    for i, h in enumerate(header):
        if h != 'Churn':
            raw = data2[h]
            raw_new = data_new[h]
            try:
                dat = raw_new.astype(np.float64)
            except ValueError:
                dat = np.zeros(raw_new.shape)
                vals = np.unique(raw)
                for j, u in enumerate(vals):
                    dat[raw_new == u.decode('UTF-8')] = j
            if (np.isnan(dat).any()):
                print(dat)
                print(h)
            for row in range(len(dat)):
                x[row][i] = dat[row][0]
    return clf.predict(x)