#
from flask import Flask, request, jsonify
import prediction
import decisiontree
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return prediction.funcion_saludo()

@app.route('/api/data')
def get_data():
    return {'key': 'value', 'hello': 'world'}

@app.route('/api/clients')
def get_clients():
    response = requests.get('http://localhost:4321/api/clients/clients')
    return response.json()

#How much time will it take to the client to get his service?
@app.route('/api/estimatedtime', methods=['POST'])
def get_estimated_time():
    historical = requests.get('http://localhost:4321/api/serviceconsumptions/serviceConsumption')
    delay = decisiontree.decisionTree(historical.json(), request.json)
    return {'request': delay}


if __name__ == '__main__':
    app.run(debug=True)