
from flask import Flask, json, request, jsonify, make_response
from python_modules import model
from flask_cors import CORS
from datetime import datetime

from python_modules import login_first_time
import hashlib
from python_modules import patient

app = Flask(__name__, static_folder='./build', static_url_path='/')
CORS(app)


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/login', methods=['POST'])
def login():
    # print(request.data)
    d = json.loads(request.data.decode('utf8').replace("'", '"'))
   
    # now = datetime.now()
    # timestamp = datetime.timestamp(now)
    # dt_object = datetime.fromtimestamp(timestamp)    
    # d['timestamp'] = timestamp

    hashed_password = hashlib.sha256(d['password'].encode()).hexdigest()
    d['password'] = hashed_password

    print(d)
    status = login_first_time.verify_login(d)

    return jsonify(status)


@app.route('/signup', methods=['POST'])
def register():
    # print(request.data)
    d = json.loads(request.data.decode('utf8').replace("'", '"'))
    
    # now = datetime.now()
    # timestamp = datetime.timestamp(now)
    # dt_object = datetime.fromtimestamp(timestamp)    
    # d['timestamp'] = timestamp

    hashed_password = hashlib.sha256(d['password'].encode()).hexdigest()
    d['password'] = hashed_password

    status = login_first_time.register_data(d)
    return jsonify(status)


@app.route('/firstchat', methods=['POST'])
def firstchat():
    d = json.loads(request.data.decode('utf8').replace("'", '"'))
    status = patient.first_chat(d)
    
    return jsonify(status)


@app.route('/chat', methods=['POST'])
def chat():
    d = json.loads(request.data.decode('utf8').replace("'", '"'))
    
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    # dt_object = datetime.fromtimestamp(timestamp)    
    d['timestamp'] = int(timestamp)

    status = patient.daily_chat(d)

    return jsonify(status)


@app.route('/test', methods=['POST'])
def get_test_results():
    d = json.loads(request.data.decode('utf8').replace("'", '"'))
    
    status = patient.test_result(d)
    
    return jsonify(status)
    

@app.route('/record/<email>')
def get_patient_records(email):

    status = patient.get_records(email)

    return jsonify(status)
    

@app.route('/patients')
def get_patient_details():

    status = patient.get_details()

    return jsonify(status)


"""
@app.route("/get_patient_first_data", methods=["GET", "POST"])
def take_input():
    if request.method == 'POST':
        data = request.get_json()
        outcome = model.predict(data)
    # if text is None:
    #    return jsonify({"message":"text not found"})

    return jsonify({"Testing_required": outcome})
"""

if __name__ == "__main__":
    login_first_time.create_db()
    app.run(debug=True)
