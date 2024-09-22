from sklearn import datasets
from sklearn.linear_model import LogisticRegression
import pickle


iris = datasets.load_iris()
X, y = iris.data, iris.target

# fit a logistic regression model to the data
def train():
    clf = LogisticRegression(max_iter=1000, random_state=0)
    clf.fit(X, y)
    print ('Model trained')
    print(f'Model Accuracy: {clf.score(X, y):0.2f}')
    return clf

def save(clf):
    with open('model.pkl', 'wb') as f:
        pickle.dump(clf, f)
    print('Model saved')    

if __name__ == '__main__':
    clf = train()
    save(clf)

