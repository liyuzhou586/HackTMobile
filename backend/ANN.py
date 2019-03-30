from sklearn.externals import joblib
import json
import numpy as np

clf = joblib.load('ANN.joblib')
data2 = np.load('data2.npy')
header = data2.dtype.names

def predict(json_input):
    table = json.loads(json_input)
    count = 0
    data = []
    for row in table:
        if count == 0:
            header = row.keys()
            data.append(list(header))
            count += 1
        data.append(list(row.values()))
    data_new = np.array(data)

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
                    dat[raw_new == u] = j
            if (np.isnan(dat).any()):
                print(dat)
                print(h)
            x[:,i] = dat
    return clf.predict(x)