from tinydb import TinyDB, Query


def create_db():
    TinyDB('tinyDB/patient_login.json')
    TinyDB('tinyDB/doctor_login.json')


def verify_login(data):
    print(data)
    return_data = {}
    query = Query()

    db = TinyDB('tinyDB/patient_login.json')

    search_result = db.search(query.Email == data['Email'])

    if(search_result):
        if(search_result[0]['Password'] == data['Password']):
            return_data['return_message'] = "Password correct"
            return_data['role'] = "Patient"
            return_data['status'] = 200

            return return_data

        else:
            return_data['return_message'] = "Password incorrect"
            return_data['role'] = "Patient"
            return_data['status'] = 500

            return return_data

    db = TinyDB('tinyDB/doctor_login.json')

    search_result = db.search(query.Email == data['Email'])

    if(search_result):
        if(search_result[0]['Password'] == data['Password']):
            return_data['return_message'] = "Password correct"
            return_data['role'] = "Doctor"
            return_data['status'] = 200

            return return_data

        else:
            return_data['return_message'] = "Password incorrect"
            return_data['role'] = "Doctor"
            return_data['status'] = 500

            return return_data

    return_data['return_message'] = "No user found"
    return_data['role'] = ""
    return_data['status'] = 500

    return return_data


def register_data(data):
    if(data['Role'] == "Doctor"):
        return register_as_doctor(data)

    elif(data['Role'] == "Patient"):
        return register_as_patient(data)


def register_as_doctor(data):
    # print(data)
    db = TinyDB('tinyDB/patient_login.json')
    return_data = {}
    query = Query()

    if(db.search(query.Email == data['Email'])):
        return_data["status"] = 500
        return_data["return_message"] = "Email id already registered as a patient"
        return return_data

    db = TinyDB('tinyDB/doctor_login.json')

    if(db.search(query.Email == data['Email'])):
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
    if(db.search(query.Email == data['Email'])):
        return_data["status"] = 500
        return_data["return_message"] = "Email id already registered as a doctor"
        return return_data

    db = TinyDB('tinyDB/patient_login.json')

    if(db.search(query.Email == data['Email'])):
        return_data["status"] = 500
        return_data["return_message"] = "Email id already registered as a patient"
        return return_data

    db.insert(data)

    return_data["return_message"] = "Successfully registered as a patient"
    return_data["status"] = 200
    return return_data
