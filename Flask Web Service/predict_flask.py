import pickle
import numpy as np
from flask import Flask, request, jsonify
from waitress import serve

url = 'http://localhost:8080/predict'
def load():
    with open('model.pkl', 'rb') as f:
        clf = pickle.load(f)
    print('Model loaded')
    return clf
clf = load()

app = Flask(__name__)
@app.route('/predict', methods=['POST'])
def predict():
    flower = request.get_json()
    flower_vals = np.array([flower['petal_length'], flower['petal_width'], flower['sepal_length'], flower['sepal_width']]).reshape(1, -1)
    pred = clf.predict(flower_vals)
    result = {'prediction': int(pred[0])}
    return jsonify(result)

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)