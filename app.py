from flask import Flask, request, json, jsonify
import model

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/<name>")
def hello_name(name):
    return "Hello " + name


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