from tinydb import TinyDB, Query
import model


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


def get_details(data):

    query = Query()

    db = TinyDB('tinyDB/patient_login.json')
    
    search_result = db.search(query.email == data)
    
    if(search_result):
        search_result = dict(search_result[0])
        search_result.pop('password')
        search_result['status'] = 200

        return search_result

    return_data = {}
    return_data['status'] = 500

    return return_data