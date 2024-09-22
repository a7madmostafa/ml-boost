import pickle
import numpy as np

def load():
    with open('model.pkl', 'rb') as f:
        clf = pickle.load(f)
    print('Model loaded')
    return clf

def predict(clf, features):
    return clf.predict(features)[0]

if __name__ == '__main__':
    clf = load()
    print('Model loaded')
    features = np.array([1, 2, 3, 4]).reshape(1, -1)
    print(predict(clf, features))