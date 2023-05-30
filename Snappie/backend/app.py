from flask import Flask, request, jsonify
from flask_cors import CORS
from prompt import prompt
app = Flask(__name__)
cors = CORS(app)

@app.route("/prompt", methods=["POST"])
def postPrompt():
    data = request.get_json()
    result = prompt(data['input'])
    data = {
        "headers": {'Content-Type':'application/json',
                    "Access-Control-Allow-Headers" : "Content-Type",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "OPTIONS,POST,GET"},
        "body": result,
        "statusCode": 200,
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)