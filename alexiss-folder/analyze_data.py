import json
import logging
from flask import Flask, request, jsonify

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

######################################################################
#fletcher:
def read_ortho_json() -> list:
    """
    Reads the JSON data from the 'ortho.json' file.
    
    Description:
    This function opens 'ortho.json' and loads the clinic data into a Python list.
    
    Args:
    no arguments

    Returns:
    list: A list of dictionaries representing orthopedic clinics from the JSON file.
    """
    try:
        with open('ortho.json', 'r') as f:
            ortho_clinic_data = json.load(f)
            logging.debug("Successfully loaded data from 'ortho.json'.")
            return ortho_clinic_data
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        return []  # Return an empty list if the file is not found
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON: {e}")
        return []  # Return an empty list if JSON is corrupted
    
@app.route('/homepage/ortho_data', methods=['GET'])
def get_clinics():
    ortho_clinic_data = read_ortho_json()  #  makes read_json function ortho_clinic_data to load the data 
    if ortho_clinic_data:
        return jsonify(ortho_clinic_data)  # return the ortho_clinic_data
    else:
        return jsonify({"error": "Unable to load clinic data"}), 500  # if nothing in the clinic_data file return this
    
#def clinic_rating_order(data: list[dict], google_review_rating: str) -> list:
  #  sorted_clinics = sorted(data, key=lambda clinic: float(clinic.get(google_review_rating, 0) or 0), reverse=True)
   # return sorted_clinics

######################################################################
#alexis:
def read_medical_imaging_json() -> list:
    try:
        with open('medical_imaging.json', 'r') as f:
            medical_imaging_data = json.load(f)
            logging.debug("Successfully loaded data from 'ortho.json'.")
            return medical_imaging_data
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        return []  # Return an empty list if the file is not found
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON: {e}")
        return []  # Return an empty list if JSON is corrupted
    
@app.route('/homepage/medical_imaging_data', methods=['GET'])
def get_medical_imaging_clinics():
    medical_imaging_data = read_medical_imaging_json()   
    if medical_imaging_data:
        return jsonify(medical_imaging_data ) 
    else:
        return jsonify({"error": "Unable to load clinic data"}), 500 
    
######################################################################

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
