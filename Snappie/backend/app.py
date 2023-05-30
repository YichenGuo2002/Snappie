from flask import Flask, request, jsonify
from flask_cors import CORS
from prompt import prompt, start
from dotenv import load_dotenv
import os
load_dotenv()
URL = os.environ.get('URL')
PORT = os.environ.get('PORT')
app = Flask(__name__)
cors = CORS(app)

@app.route("/start", methods=["POST"])
def startPrompt():
    start()
    data = {
        "headers": {'Content-Type':'application/json',
                    "Access-Control-Allow-Headers" : "Content-Type",
                    "Access-Control-Allow-Origin": '*',
                    "Access-Control-Allow-Methods": "OPTIONS,POST,GET"},
        "statusCode": 200,
    }
    return jsonify(data)

@app.route("/prompt", methods=["POST"])
def postPrompt():
    data = request.get_json()
    result = prompt(data['input'])
    data = {
        "headers": {'Content-Type':'application/json',
                    "Access-Control-Allow-Headers" : "Content-Type",
                    "Access-Control-Allow-Origin": '*',
                    "Access-Control-Allow-Methods": "OPTIONS,POST,GET"},
        "body": result,
        "statusCode": 200,
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host=URL, port=PORT, debug=True)