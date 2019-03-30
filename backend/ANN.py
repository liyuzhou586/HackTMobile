from sklearn.externals import joblib
import json
import numpy as np

clf = joblib.load('ANN.joblib')
data2 = np.load('data2.npy')
header = data2.dtype.names

def predict(json_input):
    table = json.loads(json_input)
    data_new = []
    for row in table:
        row_new = []
        for label in header:
            if label != 'Churn':
                row_new.append(row[label])
        data_new.append(row_new)
    data_new = np.array(data_new)

    x = np.zeros((len(y), len(header)))

    for i, h in enumerate(header):
        if h != 'Churn':
            raw = data2[h]
            raw_new = data_new[h]
            if raw.dtype == np.int32:
                dat = raw_new.astype(np.float64)
            elif raw.dtype == np.float64:
                dat = raw_new
            else:
                dat = np.zeros(raw_new.shape)
                vals = np.unique(raw)
                for j, u in enumerate(vals):
                    dat[raw_new == u] = j
            if (np.isnan(dat).any()):
                print(dat)
                print(h)
            x[:,i] = dat
    return clf.predict(x)