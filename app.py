from flask import Flask, jsonify  # type: ignore
from analyze_data import read_json  # Puts the read_json file from anaylze_ortho code

app = Flask(__name__)

@app.route('/api/clinics', methods=['GET'])
def get_clinics():
    clinic_data = read_json()  #  makes read_json function clinic_data to load the data 
    if clinic_data:
        return jsonify(clinic_data)  # return the clinic_data
    else:
        return jsonify({"error": "Unable to load clinic data"}), 500  # if nothing in the clinic_data file return this

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5555, debug=True)