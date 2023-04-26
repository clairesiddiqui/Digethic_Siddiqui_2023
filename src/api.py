from flask import Flask, Response, request
from flask_cors import CORS
import os
import pandas as pd
import pickle

app = Flask(__name__)

CORS(app)


training_data = pd.read_csv(os.path.join('data', 'auto-mpg.csv'))

print(training_data.head())

@app.route("/", methods=["GET"])
def index():
    return {"hello": "world"}


@app.route("/hello_world", methods=["GET"])
def hello_world():
    return "<p>Hello world!<p>"


@app.route("/training_data", methods=["GET"])
def get_training_data():
    return Response(training_data.to_json(), mimetype="application/json")


