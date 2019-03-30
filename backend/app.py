from flask import Flask, request
from util import *
from flask_cors import CORS
app = Flask(__name__)

CORS(app)


@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@app.route('/about')
def about():
    return "Call Bob if you have any question"

@app.route('/device', methods=['GET'])
def device():
    return giveUserPhoneOption()

@app.route('/queryStuff1', methods=['POST'])
def queryStuff1():
    # {"queryParam": "query sample"}
    jsonFormatParam = request.json['queryParam']
    return queryFunc1(jsonFormatParam)

if __name__ == '__main__':
    app.run()