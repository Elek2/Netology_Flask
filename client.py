import json

import requests
from requests.auth import HTTPBasicAuth


def user_get():
    response = requests.get("http://127.0.0.1:5000/user/")
    print()
    print(response.status_code)
    print(response.text)


def advert_get():
    response = requests.get("http://127.0.0.1:5000/adv/")
    print()
    print(response.status_code)
    print(response.text)


def user_post(data):
    headers = {"Content-Type": "application/json"}
    json_data = json.dumps(data)
    response = requests.post(
        "http://127.0.0.1:5000/user/",
        headers=headers,
        data=json_data,
    )
    print()
    print(response.status_code)
    print(response.text)


def advert_post(data, auth):
    headers = {"Content-Type": "application/json"}
    json_data = json.dumps(data)
    response = requests.post(
        "http://127.0.0.1:5000/adv/", headers=headers, data=json_data, auth=auth
    )
    print()
    print(response.status_code)
    print(response.text)


def advert_delete(auth, adv_id):
    response = requests.delete(f"http://127.0.0.1:5000/adv/{adv_id}", auth=auth)
    print()
    print(response.status_code)
    print(response.text)


if __name__ == "__main__":
    user1 = {
        "username": "user1",
        "email": "user1@mail.ru",
        "password": "111",
    }

    user2 = {
        "username": "user2",
        "email": "user2@mail.ru",
        "password": "222",
    }

    auth1 = HTTPBasicAuth(username=user1['email'], password=user1['password'])
    auth2 = HTTPBasicAuth(username=user2['email'], password=user2['password'])

    data1 = {
        "header": "Car",
        "description": "Buy a car",
    }

    data2 = {
        "header": "House",
        "description": "Buy a house",
    }

    user_post(user1)  # 200
    user_post(user2)  # 200
    user_get()  # 200

    advert_post(data1, auth1)  # 200
    advert_post(data2, auth2)  # 200
    advert_post(data2, None)  # 401 Unauthorized Access

    advert_delete(auth2, 1)  # 409 can't delete other user's adv
    advert_delete(auth2, 3)  # 404 no advertisement
    advert_delete(auth2, 2)  # 200 ок


