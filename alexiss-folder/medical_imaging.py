import json
import logging

from flask import Flask, request


app = Flask(__name__)

# Helper function to retrieve data from the movies.json file

def get_data() -> list[dict]:
    """
    Retrieve the movies dataset and return it as a list of dictionaries.

    Returns:
        data (list[dict]): A list of dictionaries containing the movies dataset.
    """
    with open('medical_imaging.json', 'r') as file:
        data = json.load(file)
    return data

# TODO: Add a route to return the entire dataset
@app.route('/medical-imaging-data', methods=['GET'])
def medical_imaging_data():
    return get_data()