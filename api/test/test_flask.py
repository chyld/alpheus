import pytest

import requests


@pytest.fixture
def clear():
    requests.get('http://localhost:5000/clear')


def test_status():
    response = requests.get('http://localhost:5000/status')
    response = response.json()
    assert response['status'] == 'ok'


def test_clear():
    response = requests.get('http://localhost:5000/clear')
    response = response.json()
    assert response['status'] == 'cleared'


def test_append(clear):
    requests.get('http://localhost:5000/append/3')
    response = requests.get('http://localhost:5000/append/5')
    response = response.json()
    assert response['list'] == '3 -> 5'


def test_prepend(clear):
    requests.get('http://localhost:5000/prepend/3')
    response = requests.get('http://localhost:5000/prepend/5')
    response = response.json()
    assert response['list'] == '5 -> 3'


def test_reverse(clear):
    requests.get('http://localhost:5000/append/1')
    requests.get('http://localhost:5000/append/2')
    response = requests.get('http://localhost:5000/reverse')
    response = response.json()
    assert response['list'] == '2 -> 1'


def test_find(clear):
    requests.get('http://localhost:5000/append/1')
    requests.get('http://localhost:5000/append/2')
    requests.get('http://localhost:5000/append/3')
    response = requests.get('http://localhost:5000/find/2')
    response = response.json()
    assert response['found'] == 'True'
    response = requests.get('http://localhost:5000/find/4')
    response = response.json()
    assert response['found'] == 'False'
