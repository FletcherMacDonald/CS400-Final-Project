import json
import logging
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_cors import CORS  # Correct import for CORS
import os

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

        # Read JSON based on clinic type
        if clinic_type == 'Orthopedics':
            clinics = read_ortho_json()
            filename = 'ortho.json'
        elif clinic_type == 'Medical Imaging':
            clinics = read_medical_imaging_json()
            filename = 'medical_imaging.json'
        elif clinic_type == 'Physical Therapy':
            clinics = read_pt_json()
            filename = 'pt.json'
        else:
            return jsonify({"error": "Invalid clinic type selected."}), 400
        
        default_image = 'No_image_available.svg.png'

        # Collect form data and store it in the appropriate keys
        new_clinic = {
            "type": clinic_type,
            "clinic_name": request.form['clinic_name'],  # Match the 'clinic_name' field from the form
            "address": request.form['address'],
            "phone_number": request.form['phone_number'],
            "clinic_hours": request.form['clinic_hours'],  # Match the 'clinic_hours' field from the form
            "private_or_public": request.form['private_or_public'],  # Match the 'private_or_public' field
            "google_review_rating": float(request.form['google_review_rating']),  # Match the 'google_review_rating' field
            "head_doctor": request.form['head_doctor'],
            "date_of_establishment": request.form['date_of_establishment'],  # Match the 'date_of_establishment' field
            "image_name": default_image
        }

        # Append the new clinic to the list of clinics
        clinics.append(new_clinic)

        # Save the updated list back to the correct JSON file
        with open(filename, 'w') as f:
            json.dump(clinics, f, indent=4)

        logging.debug(f"New {clinic_type} clinic added successfully to {filename}.")

        # Redirect to the success page after the form submission
        return redirect(url_for('success_page'))

    # If GET request, show the form
    return render_template('add-clinic.html')

@app.route('/success')
def success_page():
    return render_template('success.html')

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
            logging.debug("Successfully loaded data from 'medical_imaging.json'.")
            return medical_imaging_clinic_data
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        return []  # Return an empty list if the file is not found
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON: {e}")
        return []  # Return an empty list if JSON is corrupted
    
@app.route('/medical-imaging_data', methods=['GET'])
def get_medical_imaging_clinics():
    medical_imaging_clinic_data = read_medical_imaging_json()  
    if medical_imaging_clinic_data:
        return jsonify(medical_imaging_clinic_data )  
    else:
        return jsonify({"error": "Unable to load clinic data"}), 500 

@app.route('/medical-imaging-page')
def medical_imaging_page():
    """
    Renders the medical imaging page and passes clinic data to the template.
    """
    medical_imaging_clinic_data = read_medical_imaging_json() 
    return render_template('medical-imaging.html', clinics=medical_imaging_clinic_data)  

#Delete request:
"""
Example:
@app.route('/delete/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    movie = db.session.get(Movie, movie_id)
    if movie:
        db.session.delete(movie)
        db.session.commit()
    return f'Movie: {movie.title}', 204
"""

@app.route('/delete/<clinic_name>', methods=['DELETE'])
def delete_clinic_by_name(clinic_name):
    json_path = 'medical_imaging.json'

    if not os.path.exists(json_path):
        return 'Data file not found.', 500
    with open(json_path, 'r') as f:
        clinics = json.load(f)
    
    updated_clinics = [clinic for clinic in clinics if clinic['clinic_name'] != clinic_name]
    
    if len(updated_clinics) == len(clinics):
        return f'Clinic "{clinic_name}" not found.', 404

    #save the updated list
    with open(json_path, 'w') as f:
        json.dump(updated_clinics, f, indent=4)

    return f'Clinic "{clinic_name}" deleted successfully.', 204

######################################################################
#wilneris!
def read_pt_json() -> list:
    """
    Reads JSON data from the 'pt.json' file.
    
    Description:
    This function opens 'pt.json' and loads the clinic data list.
    
    Returns:
    list: A list of dictionaries representing pt clinics.
    """
    try:
        with open('pt.json', 'r') as f:
            pt_clinic_data = json.load(f)
            logging.debug("Successfully loaded data from 'pt.json'.")
            return pt_clinic_data
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        return []  # return an empty list if the file is not found
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding pt.JSON: {e}")
        return []  # return an empty list if JSON is corrupted
    
@app.route('/pt_data', methods=['GET'])
def get_pt_clinics():
    pt_clinic_data = read_pt_json()  
    if pt_clinic_data :
        return jsonify(pt_clinic_data)  # return data
    else:
        return jsonify({"error": "Unable to load clinic data"}), 500 

@app.route('/pt-page')
def pt_page():
    pt_clinic_data = read_pt_json() # Get the clinic data from the JSON file
    return render_template('pt.html', clinics=pt_clinic_data)  # Pass the data to the template

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