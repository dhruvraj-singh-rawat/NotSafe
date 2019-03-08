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

def lcs(X , Y): 
# find the length of the strings 
    m = len(X) 
    n = len(Y) 

    # declaring the array for storing the dp values 
    L = [[None]*(n+1) for i in range(m+1)] 

    """Following steps build L[m+1][n+1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1]) 

    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1] 
    return L[m][n] 
    #end of function lcs 

def checkForSimilarity(password):
    filePath = "../AIGeneratedPasswords/"
    fileName = filePath + "generated_passwords.txt"
    maxPercentage = 0
    with open(fileName, 'r') as f:    
        for AIPassword in f:
            try:
                strippedAIPassword = AIPassword.strip('\n')
                if(password == strippedAIPassword):
                    print("GIVING TRUE")
                    return 100
                else:
                    lcsLength = lcs(password, strippedAIPassword)
                    similarityPercentage = lcsLength/max(len(password), len(strippedAIPassword))*100
                    maxPercentage = max(maxPercentage, similarityPercentage)
            except IndexError:
                print ("A line in the file doesn't have enough entries.")
        return maxPercentage

@app.route('/compute-strength', methods=['POST', 'OPTIONS'])
def compute_password_strength():
    if request.method == 'OPTIONS':
        return jsonify({'success': "false"})
    if not request.json or not 'title' in request.json:
        jsonify({'success': "false"})
        password = request.json['password']
        similarityPercentage = checkForSimilarity(password)
    return jsonify({'success': "true", "similarityPercentage": round(similarityPercentage, 2)}), 201

if __name__ == '__main__':
    app.run(debug=True)