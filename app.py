from flask import Flask, request, jsonify, render_template, make_response
import model
import json
from flask_cors import CORS

app = Flask(__name__, static_folder='./build', static_url_path='/')
CORS(app)


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/login', methods=['POST'])
def login():
	print(request.data)
	d = request.data.decode('utf8').replace("'", '"')
	print(d)
	return make_response(jsonify(d), 200)


@app.route("/get_patient_first_data", methods=["GET", "POST"])
def take_input():
	if request.method == 'POST':
		data = request.get_json()
		outcome = model.predict(data)
	# if text is None:
	#    return jsonify({"message":"text not found"})

	return jsonify({"Testing_required": outcome})


if __name__ == "__main__":
    app.run(debug=True)
