from tinydb import TinyDB, Query


def create_db():
    TinyDB('tinyDB/patient_login.json')
    TinyDB('tinyDB/doctor_login.json')
    TinyDB('tinyDB/patients_history.json')


def verify_login(data):
    print(data)
    return_data = {}
    query = Query()

    db = TinyDB('tinyDB/patient_login.json')

    search_result = db.search(query.email == data['email'])

    if(search_result):
        if(search_result[0]['password'] == data['password']):
            return_data['return_message'] = "Password correct"
            return_data['role'] = "patient"
            
            return_data['name'] = search_result[0]['name']
            return_data['age'] = search_result[0]['age']
            return_data['gender'] = search_result[0]['gender']
            return_data['status'] = 200

            return return_data

        else:
            return_data['return_message'] = "Password incorrect"
            return_data['role'] = "patient"
            return_data['status'] = 500

            return return_data

    db = TinyDB('tinyDB/doctor_login.json')

    search_result = db.search(query.email == data['email'])

    if(search_result):
        if(search_result[0]['password'] == data['password']):
            return_data['return_message'] = "Password correct"
            return_data['role'] = "doctor"
            return_data['status'] = 200

            return return_data

        else:
            return_data['return_message'] = "Password incorrect"
            return_data['role'] = "doctor"
            return_data['status'] = 500

            return return_data

    return_data['return_message'] = "No user found"
    return_data['role'] = ""
    return_data['status'] = 500

    return return_data


def register_data(data):
    if(data['role'] == "doctor"):
        return register_as_doctor(data)

    elif(data['role'] == "patient"):
        return register_as_patient(data)


def register_as_doctor(data):
    print(data)
    db = TinyDB('tinyDB/patient_login.json')
    return_data = {}
    query = Query()

    if(db.search(query.email == data['email'])):
        return_data["status"] = 500
        return_data["return_message"] = "Email id already registered as a patient"
        return return_data

    db = TinyDB('tinyDB/doctor_login.json')

    if(db.search(query.email == data['email'])):
        return_data["status"] = 500
        return_data["return_message"] = "Email id already registered as a doctor"
        return return_data

    db.insert(data)
    return_data["return_message"] = "Successfully registered as a doctor"
    return_data["status"] = 200
    return return_data


def register_as_patient(data):
    # print(data)
    db = TinyDB('tinyDB/doctor_login.json')

    return_data = {}
    query = Query()
    if(db.search(query.email == data['email'])):
        return_data["status"] = 500
        return_data["return_message"] = "Email id already registered as a doctor"
        return return_data

    db = TinyDB('tinyDB/patient_login.json')

    if(db.search(query.email == data['email'])):
        return_data["status"] = 500
        return_data["return_message"] = "Email id already registered as a patient"
        return return_data

    db.insert(data)

    return_data["return_message"] = "Successfully registered as a patient"
    return_data["status"] = 200
    return return_data
