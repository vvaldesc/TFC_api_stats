#
from flask import Flask, request, jsonify
import prediction
import decisiontree
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return prediction.funcion_saludo()

#How much time will it take to the client to get his service?
@app.route('/api/estimatedtime', methods=['POST'])
def get_estimated_time():
    historical = requests.get('http://localhost:4321/api/serviceconsumptions/serviceConsumptions')
    delay = decisiontree.decisionTree(historical.json(), request.json)
    return {'request': delay}

if __name__ == '__main__':
    app.run(debug=True)