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


@app.route('/add-clinic-page', methods=['GET', 'POST'])
def viewer_input():
    if request.method == 'POST':
        clinic_type = request.form['clinic_type']

        if clinic_type == 'Orthopedics':
            clinics = read_ortho_json()
            filename = 'ortho.json'
        elif clinic_type == 'Medical Imaging':
            clinics = read_medical_imaging_json()
            filename = 'medical_imaging.json'
        elif clinic_type == 'Physical Therapy':
            clinics = read_physio_json()
            filename = 'physio.json'
        else:
            return jsonify({"error": "Invalid clinic type selected."}), 400

        new_clinic = {
            "type": clinic_type,
            "name": request.form['name'],
            "address": request.form['address'],
            "hours": request.form['hours'],
            "ownership": request.form['public_private'],
            "rating": float(request.form['rating']),
            "head_doctor": request.form['head_doctor'],
            "date_established": request.form['date_established']
        }

        clinics.append(new_clinic)

        # Save back to the correct JSON file
        with open(filename, 'w') as f:
            json.dump(clinics, f, indent=4)

        logging.debug(f"New {clinic_type} clinic added successfully to {filename}.")

        return jsonify({"message": f"{clinic_type} clinic added successfully!"}), 200

    # If GET request, show the form
    return render_template('add-clinic.html')

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
def read_physio_json() -> list:
    """
    Reads JSON data from the 'physio.json' file.
    
    Description:
    This function opens 'pysio.json' and loads the clinic data list.
    
    Returns:
    list: A list of dictionaries representing physiotherapy clinics.
    """
    try:
        with open('physio.json', 'r') as f:
            physio_clinic_data = json.load(f)
            logging.debug("Successfully loaded data from 'physio.json'.")
            return physio_clinic_data
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        return []  # return an empty list if the file is not found
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding PHYSIO.JSON: {e}")
        return []  # return an empty list if JSON is corrupted
    
@app.route('/physiotherapy_data', methods=['GET'])
def get_physiotherapy_clinics():
    medical_imaging_clinic_data = read_physio_json()  
    if medical_imaging_clinic_data:
        return jsonify(medical_imaging_clinic_data )  # return data
    else:
        return jsonify({"error": "Unable to load clinic data"}), 500 

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