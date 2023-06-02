import json

import requests
from requests.auth import HTTPBasicAuth


def user_get():
    headers = {}
    params = {}
    response = requests.get("http://127.0.0.1:5000/user/", headers=headers)
    print(response.text)


def advert_get():
    headers = {}
    response = requests.get("http://127.0.0.1:5000/adv/", headers=headers)
    print(response.text)


def user_post():
    headers = {'Content-Type': 'application/json'}
    data = {
        'username': 'Mura',
        'email': 'mura@mail.ru',
        'password': '222',
    }
    json_data = json.dumps(data)
    response = requests.post(
        "http://127.0.0.1:5000/user/",
        headers=headers,
        data=json_data,
    )
    print(response.text)

def advert_post():
    headers = {'Content-Type': 'application/json'}
    basic = HTTPBasicAuth('mura@mail.ru', '222')
    data = {
        'header': 'Car',
        'description': 'Buy a car',
    }
    json_data = json.dumps(data)
    a = requests
    response = requests.post("http://127.0.0.1:5000/adv/", headers=headers, data=json_data, auth=basic)
    print(response.text)

def advert_delete():
    headers = {'Content-Type': 'application/json'}
    response = requests.delete("http://127.0.0.1:5000/adv/1")
    print(response.text)


# user_post()
advert_post()

