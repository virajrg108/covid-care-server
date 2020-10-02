from tinydb import TinyDB, Query
from python_modules import model


def first_chat(data):
    #print(data)
    return_data = {}
    query = Query()

    db = TinyDB('tinyDB/patient_login.json')

    search_result = db.search(query.email == data['email'])

    return_data['status'] = 200
    return_data['testRequired'] = model.predict(data)

    data['testRequired'] = return_data['testRequired']

    db.update( data, query.email == data['email'])

    return return_data


def daily_chat(data):
    #print(data)
    return_data = {}
    query = Query()

    db = TinyDB('tinyDB/patients_history.json')

    db.insert(data)

    return_data['status'] = 200
    return return_data


def get_records(data):

    return_data = {}
    query = Query()

    db = TinyDB('tinyDB/patients_history.json')
    
    return_data['result'] = db.search(query.email == data)
    return_data['status'] = 200

    return return_data


def get_details():

    query = Query()
    return_data = {}

    db = TinyDB('tinyDB/patient_login.json')
    
    #search_result = db.search(query.email == data)
    
    all_patients_details = db.all()

    for patient_detail in all_patients_details:
        patient_detail.pop('password')

    return_data['data'] = all_patients_details
    return_data['status'] = 200

    return return_data


def test_result(data):

    return_data = {}
    query = Query()

    db = TinyDB('tinyDB/patient_login.json')

    search_result = db.search(query.email == data['email'])

    corads = data['corads']
    hrct = data['hrct']

    return_data['status'] = 200
    return_data['testResult'] = model.severity(corads, hrct)

    data['testResult'] = return_data['testResult']

    db.update( data, query.email == data['email'])

    return return_data