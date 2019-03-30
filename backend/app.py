from flask import Flask, request 
from util import *
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        return doSomething(request.json)
    else:
        return giveUserPhoneOption()

if __name__ == '__main__':
    app.run()