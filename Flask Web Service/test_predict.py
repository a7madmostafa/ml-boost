import requests

flower = {
    "petal_length": 5.1,
    "petal_width": 3.5,
    "sepal_length": 1.4,
    "sepal_width": 0.2
}

url = 'http://localhost:8080/predict'
response = requests.post(url, json=flower)
result = response.json()
print(result)