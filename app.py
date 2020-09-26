
from flask import Flask, json, request, jsonify, make_response
import model
from flask_cors import CORS
from datetime import datetime
import tiny
import hashlib

app = Flask(__name__, static_folder='./build', static_url_path='/')
CORS(app)


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/login', methods=['POST'])
def login():
    #print(request.data)
    d = json.loads(request.data.decode('utf8').replace("'", '"'))
   
    #now = datetime.now()
    #timestamp = datetime.timestamp(now)
    #dt_object = datetime.fromtimestamp(timestamp)    
    #d['timestamp'] = timestamp

    hashed_password = hashlib.sha256(d['Password'].encode()).hexdigest()
    d['Password'] = hashed_password

    print(d)
    status = tiny.verify_login(d)

    return jsonify(status)

@app.route('/register', methods=['POST'])
def register():
    #print(request.data)
    d = json.loads(request.data.decode('utf8').replace("'", '"'))
    
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    #dt_object = datetime.fromtimestamp(timestamp)    
    d['timestamp'] = timestamp

    hashed_password = hashlib.sha256(d['Password'].encode()).hexdigest()
    d['Password'] = hashed_password

    status = tiny.register_data(d)
    return jsonify(status)


@app.route("/get_patient_first_data", methods=["GET", "POST"])
def take_input():
    if request.method == 'POST':
        data = request.get_json()
        outcome = model.predict(data)
    # if text is None:
    #    return jsonify({"message":"text not found"})

    return jsonify({"Testing_required": outcome})


if __name__ == "__main__":
    tiny.create_db()
    app.run(debug=True)
