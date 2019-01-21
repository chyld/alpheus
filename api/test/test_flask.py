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
    requests.get('http://localhost:5000/append/3.14')
    response = requests.get('http://localhost:5000/append/2.71')
    response = response.json()
    assert response['list'] == '3.14 -> 2.71'
