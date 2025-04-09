import json
import logging
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # Correct import for CORS

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

@app.route('/')
def home():
    """
    Renders the index.html page and passes clinic data to the template.
    """
    ortho_clinic_data = read_ortho_json()
    return render_template('index.html', clinics=ortho_clinic_data)

def read_ortho_json() -> list:
    """
    Reads the JSON data from the 'ortho.json' file.
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

@app.route('/ortho_data', methods=['GET'])
def get_ortho_clinics():
    """
    Returns orthopedic clinic data in JSON format.
    """
    ortho_clinic_data = read_ortho_json()  # Fetch clinic data for the /homepage/ortho_data endpoint
    if ortho_clinic_data:
        return jsonify(ortho_clinic_data)  # Return the clinic data in JSON format
    else:
        return jsonify({"error": "Unable to load clinic data"}), 500  # If no data is found

@app.route('/orthopedics-page')
def orthopedics():
    """
    Renders the orthopedics page and passes clinic data to the template.
    """
    ortho_clinic_data = read_ortho_json()  # Get the clinic data from the JSON file
    return render_template('orthopedics.html', clinics=ortho_clinic_data)  # Pass the data to the template


@app.route('/homepage/viewer_imput', methods=['POST'])
def viewer_input():
    global ortho_clinic_data
    
    add_clinic_name = input("clinic_name");
    return "it working"
    # add_phone_number = input("phone_number");
    # add_google_review_rating = input("google_review_rating");
    # add_clinic_hours = input("clinic_hours");
    # add_head_doctor = input("head_doctor");
    # add_date_of_establishment = input("date_of_establishment");
    # add_private_or_public = input("private_or_public ");

      # if nothing in the clinic_data file return this
#def clinic_rating_order(data: list[dict], google_review_rating: str) -> list:
  #  sorted_clinics = sorted(data, key=lambda clinic: float(clinic.get(google_review_rating, 0) or 0), reverse=True)
   # return sorted_clinics

######################################################################
#alexis
def read_medical_imaging_json() -> list:
    """
    Reads the JSON data from the 'medical-imaging.json' file.
    
    Description:
    This function opens 'medical-imaging.json' and loads the clinic data into a Python list.
    
    Args:
    no arguments

    Returns:
    list: A list of dictionaries representing medical imaging clinics from the JSON file.
    """
    try:
        with open('medical_imaging.json', 'r') as f:
            medical_imaging_clinic_data = json.load(f)
            logging.debug("Successfully loaded data from 'ortho.json'.")
            return medical_imaging_clinic_data
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        return []  # Return an empty list if the file is not found
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON: {e}")
        return []  # Return an empty list if JSON is corrupted
    
#@app.route('/homepage/medical-imaging_data', methods=['GET'])
@app.route('/medical-imaging_data', methods=['GET'])
def get_medical_imaging_clinics():
    medical_imaging_clinic_data = read_medical_imaging_json()  #  makes read_json function ortho_clinic_data to load the data 
    if medical_imaging_clinic_data:
        return jsonify(medical_imaging_clinic_data )  # return the ortho_clinic_data
    else:
        return jsonify({"error": "Unable to load clinic data"}), 500 

@app.route('/medical-imaging-page')
def medical_imaging_page():
    """
    Renders the medical imaging page and passes clinic data to the template.
    """
    medical_imaging_clinic_data = read_medical_imaging_json() # Get the clinic data from the JSON file
    return render_template('medical-imaging.html', clinics=medical_imaging_clinic_data)  # Pass the data to the template

######################################################################
#wilneris!
def read_pt_json() -> list:
    try:
        with open('pt.json', 'r') as f:
            pt_data = json.load(f)
            logging.debug("Successfully loaded data from 'ortho.json'.")
            return pt_data
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        return []  # Return an empty list if the file is not found
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON: {e}")
        return []  # Return an empty list if JSON is corrupted
    

@app.route('/pt-data', methods=['GET'])
def get_pt_clinics():
    pt_data = read_pt_json()  #  makes read_json function ortho_clinic_data to load the data 
    if pt_data:
        return jsonify(pt_data)  # return the ortho_clinic_data
    else:
        return jsonify({"error": "Unable to load clinic data"}), 500 

@app.route('/pt-page')
def pt_page():

    pt_clinic_data = read_pt_json() # Get the clinic data from the JSON file
    return render_template('physical-therapy.html', clinics=pt_clinic_data) 

######################################################################
#about us page
@app.route('/about-us-page')
def about_us_page():
    """
    Renders the about-us.html page
    """
    return render_template('about-us.html')

######################################################################
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5555)