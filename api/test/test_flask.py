import requests


def test_status():
    response = requests.get('http://localhost:5000/status')
    response = response.json()
    assert response['status'] == 'ok'


def test_clear():
    response = requests.get('http://localhost:5000/clear')
    response = response.json()
    assert response['status'] == 'cleared'
