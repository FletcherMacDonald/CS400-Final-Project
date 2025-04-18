import pytest
import requests
import logging


#TESTING OUR THREE GET REQUESTS: #############################################################
#1:
def test_get_ortho_clinics():
    response1 = requests.get('http://127.0.0.1:5555/ortho_data')

    logging.debug(f"Response from /ortho_data: {response1.json()}")

    assert response1.status_code == 200
    assert isinstance(response1.json(), list) == True
    assert len(response1.json()) == 8

    assert response1.json()[0]['clinic_name'] == "All Access Ortho Oahu LLC"
    assert response1.json()[0]['address'] == "1401 South Beretania Street, Suite 102, Honolulu, HI 96814"

#2: 
def test_get_medical_imaging_clinics():
    response2 = requests.get('http://127.0.0.1:5555/medical-imaging_data')

    logging.debug(f"Response from /medical_imaging-data: {response2.json()}")

    assert response2.status_code == 200
    assert isinstance(response2.json(), list) == True
    assert len(response2.json()) == 8

    assert response2.json()[2]['clinic_name'] == "Invision Imaging -- Medical Arts Building"
    assert response2.json()[2]['address'] == "1010 S King St #109, Honolulu, HI 96814"

#3:
def test_get_pt_clinics():
    response2 = requests.get('http://127.0.0.1:5555/pt_data')

    logging.debug(f"Response from /pt-data: {response2.json()}")

    assert response2.status_code == 200
    assert isinstance(response2.json(), list) == True
    assert len(response2.json()) == 8

    assert response2.json()[0]['clinic_name'] == "Moon Physical Therapy"
    assert response2.json()[0]['address'] == "95-1057 Ainamakua Dr, Mililani, HI 96789"

#TESTING OUR POST REQUEST: #############################################################
#4:
def test_viewer_input():
    url = "http://127.0.0.1:5555/add-clinic-page"
    form_data = {
        "clinic_type": "Orthopedics",
        "clinic_name": "CS-401 Orthopedics",
        "address": "3140 Waialae Ave Honolulu, HI 96816",
        "phone_number": "808-111-1111",
        "clinic_hours": "Mon-Fri 9am-5pm",
        "private_or_public": "Private",
        "google_review_rating": "5",
        "head_doctor": "Dr. Phil",
        "date_of_establishment": "2025-01-01"
    }

    response = requests.post(url, data=form_data, allow_redirects=True)

    assert response.status_code == 200
    assert "success" in response.text.lower()

#TESTING OUR DELETE REQUEST: #############################################################
#5 :
def test_delete_clinic_by_name():
    clinic_name = "Kuakini Plaza Imaging"
    url = f"http://127.0.0.1:5555/delete/{clinic_name}"
    response = requests.delete(url)
    print(response.status_code)
    assert response.status_code == 204