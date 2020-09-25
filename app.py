from flask import Flask, request, json, jsonify, render_template
import model

app = Flask(__name__, static_folder='./build', static_url_path='/')

@app.route('/')
def index():
    return app.send_static_file('index.html')


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