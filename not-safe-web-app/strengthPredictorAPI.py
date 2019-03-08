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

def checkForSimilarity(password):
    filePath = "../AIGeneratedPasswords/"
    fileName = filePath + "generated.txt"
    with open(fileName, 'r') as f:    
        for AIPassword in f:
            try:
                print(AIPassword, end='')
                print(password, end='')
                if(password == AIPassword):
                    print("GIVING TRUE")
                    return True
                else:
                    print("GIVING FALSE")
            except IndexError:
                print ("A line in the file doesn't have enough entries.")
        return False

@app.route('/compute-strength', methods=['POST', 'OPTIONS'])
def compute_password_strength():
    if request.method == 'OPTIONS':
        return jsonify({'success': "false"})
    if not request.json or not 'title' in request.json:
        jsonify({'success': "false"})
        password = request.json['password']
        isPresent = checkForSimilarity(password)
    return jsonify({'success': "true", "password": isPresent}), 201

if __name__ == '__main__':
    app.run(debug=True)