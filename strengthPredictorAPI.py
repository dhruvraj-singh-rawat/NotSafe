from flask import Flask, jsonify, request
try:
    from flask_cors import CORS  # The typical way to import flask-cors
except ImportError:
    # Path hack allows examples to be run without installation.
    import os
    parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.sys.path.insert(0, parentdir)

    from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'*', headers='Content-Type')

@app.route("/")
def hello():
    return jsonify({"about": "Hello World!"})

@app.route('/compute-strength', methods=['POST', 'OPTIONS'])
def compute_password_strength():
    if request.method == 'OPTIONS':
        return jsonify({'success': "false"})
    if not request.json or not 'title' in request.json:
        jsonify({'success': "false"})
        password = request.json['password']
    return jsonify({'success': "true"}), 201

if __name__ == '__main__':
    app.run(debug=True)