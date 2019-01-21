# export FLASK_APP=main.py FLASK_ENV=development
# flask run

from api.models.single_linked_list import SingleLinkedList

from flask import Flask, jsonify


app = Flask(__name__)
sll = SingleLinkedList()


@app.route('/status')
def status():
    return jsonify({'status': 'ok'})


@app.route('/clear')
def clear():
    sll.clear()
    return jsonify({'status': 'cleared'})


@app.route('/append/<float:val>')
def append(val):
    sll.append(val)
    return jsonify({'list': str(sll)})


@app.route('/prepend/<float:val>')
def prepend(val):
    sll.prepend(val)
    return jsonify({'list': str(sll)})


@app.route('/reverse')
def reverse():
    global sll
    sll = sll.reverse()
    return jsonify({'list': str(sll)})
