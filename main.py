#
from flask import Flask, request
import json
import regressiontree
import requests
from flask_cors import CORS
import os

FLASK_APP = os.environ.get("FLASK_APP", "main.py")
FLASK_ENV = os.environ.get("FLASK_ENV", "False")
USE_SAMPLE_DATA = os.environ.get("USE_SAMPLE_DATA", "False")

app = Flask(__name__)
CORS(app)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Usa el puerto definido por Render o 5000 por defecto
    app.run(host='0.0.0.0', port=port, debug=False)  # Asegúrate de desactivar el modo debug en producción
# CORS(app, resources={r"/api/*": {"origins": "https://localhost:4322"}})

#How much time will it take to the client to get his service?
@app.route('/api/estimatedtime', methods=['POST'])
def get_estimated_time():
    delay = regressiontree.regressiontree(None, request.json, loadTrained = True)
    return delay

@app.route('/api/estimatedtime/noTrain', methods=['POST'])
def get_estimated_time_noTrain():
    if USE_SAMPLE_DATA == "True":
        with open('sampleData.json', 'r') as file:
            historical = json.load(file)
    else:
        response = requests.get('http://localhost:4321/api/serviceConsumptions/serviceConsumptions')
        historical = response.json()
    delay = regressiontree.regressiontree(historical, request.json, loadTrained = False)
    return delay

#Train my model
@app.route('/api/estimatedtime/train', methods=['POST'])
def train_model():
    # Is the app in development mode?
    if FLASK_ENV == "development":
        if USE_SAMPLE_DATA == "True":
            with open('sampleData.json', 'r') as file:
                historical = json.load(file)
        else:
            response = requests.get('http://localhost:4321/api/serviceConsumptions/serviceConsumptions')
            historical = response.json()
        delay = regressiontree.regressiontree(historical, request.json, loadTrained=False, test=True)
        return delay
    else:
        return "Not in development mode."

#say hi
@app.route('/api/hi', methods=['GET'])
def hi():
    return 'Hola mundo'
    