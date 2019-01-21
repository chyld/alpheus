import requests


def test_status():
    response = requests.get('http://localhost:5000/status')
    response = response.json()
    assert response['status'] == 'ok'


# def test_status():
#     response = requests.get('http://localhost:5000/append/3.14')
#     response = response.json()
#     print(response)
#     assert 1 == 2
#     # assert response['status'] == 'a'
