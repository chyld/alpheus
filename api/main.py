# export FLASK_APP=hello.py
# export FLASK_ENV=development
# flask run

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify({'status': "ok"})
