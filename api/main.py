# export FLASK_APP=main.py FLASK_ENV=development
# flask run

from api.models.single_linked_list import SingleLinkedList

from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/status')
def hello_world():
    return jsonify({'status': 'ok'})
