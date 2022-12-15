from flask import Flask, request
from Api import textDetection
from ConnectDB import connectBD

app = Flask('Text Detector')

@app.route('/pythonapi', methods=['POST'])
def getImage():

    body = request.get_json()

    text = textDetection(body[0])

    return text

@app.route('/signup', methods=['POST'])
def connectionDB():

    body = request.get_json()

    print(f'Body: {body}')

    conn = connectBD(body['userEmail'], body['userPassword'])

    return conn

app.run(debug=True)