from flask import Flask
app = Flask(__name__)

import numpy as np

@app.route('/')
def home():
    return 'Hola, mundo desde Flask!'

@app.route('/api/data')
def get_data():
    return {'key': 'value', 'hello': 'world'}

if __name__ == '__main__':
    app.run(debug=True)