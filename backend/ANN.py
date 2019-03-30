from sklearn.externals import joblib

clf = joblib.load('ANN.joblib')
data2 = np.load('data2.npy')
header = data2.dtype.names

def predict(csv):
    data_new = np.genfromtxt(csv, dtype=None,
        delimiter=',', names=True, filling_values=0.0)
    y = data_new[header[0]]
    x = np.zeros((len(y), len(header) - 1))

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