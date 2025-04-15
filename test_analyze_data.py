import pytest
import requests
import logging


#TESTING OUR THREE GET REQUESTS: #############################################################
#1st:
def test_get_ortho_clinics():
    response1 = requests.get('http://127.0.0.1:5555/ortho_data')

    logging.debug(f"Response from /ortho_data: {response1.json()}")

    assert response1.status_code == 200
    assert isinstance(response1.json(), list) == True
    assert len(response1.json()) == 8

    assert response1.json()[0]['clinic_name'] == "All Access Ortho Oahu LLC"
    assert response1.json()[0]['address'] == "1401 South Beretania Street, Suite 102, Honolulu, HI 96814"
#2nd: 
def test_get_medical_imaging_clinics():
    response2 = requests.get('http://127.0.0.1:5555/medical-imaging_data')

    logging.debug(f"Response from /medical_imaging-data: {response2.json()}")

    assert response2.status_code == 200
    assert isinstance(response2.json(), list) == True
    assert len(response2.json()) == 8

    assert response2.json()[2]['clinic_name'] == "Invision Imaging -- Medical Arts Building"
    assert response2.json()[2]['address'] == "1010 S King St #109, Honolulu, HI 96814"
#3rd:
def test_get_pt_clinics():
    response2 = requests.get('http://127.0.0.1:5555/pt_data')

    logging.debug(f"Response from /pt-data: {response2.json()}")

    assert response2.status_code == 200
    assert isinstance(response2.json(), list) == True
    assert len(response2.json()) == 8

    assert response2.json()[0]['clinic_name'] == "Moon Physical Therapy"
    assert response2.json()[0]['address'] == "95-1057 Ainamakua Dr, Mililani, HI 96789"


#TESTING OUR POST REQUEST: #############################################################

def test_viewer_input():
    pass

#TESTING OUR DELETE REQUEST: #############################################################

def delete_clinic_by_name(clinic_name):         #delete a medical imaging clinic
    pass