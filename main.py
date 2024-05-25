#
from flask import Flask, request, jsonify
import regressiontree
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

CORS(app, resources={r"/api/*": {"origins": "https://localhost:4322"}})

#How much time will it take to the client to get his service?
@app.route('/api/estimatedtime', methods=['POST'])
def get_estimated_time():
    historical = requests.get('http://localhost:4321/api/serviceConsumptions/serviceConsumptions')
    delay = regressiontree.regressiontree(historical.json(), request.json, loadTrained = True)
    return delay

@app.route('/api/estimatedtime/noTrain', methods=['POST'])
def get_estimated_time_noTrain():
    historical = requests.get('http://localhost:4321/api/serviceConsumptions/serviceConsumptions')
    delay = regressiontree.regressiontree(historical.json(), request.json, loadTrained = False)
    return delay

#How much time will it take to the client to get his service?
@app.route('/api/estimatedtime/fiability', methods=['POST'])
def get_roc_curve():
    historical = requests.get('http://localhost:4321/api/serviceConsumptions/serviceConsumptions')
    delay = regressiontree.regressiontree(historical.json(), request.json, test=True, loadTrained = True)
    return delay

#Train my model
@app.route('/api/estimatedtime/train', methods=['POST'])
def train_model():
    historical = requests.get('http://localhost:4321/api/serviceConsumptions/serviceConsumptions')
    delay = regressiontree.regressiontree(historical.json(), request.json, loadTrained = False, test=True)
    return delay
    

if __name__ == '__main__':
    app.run(debug=True)