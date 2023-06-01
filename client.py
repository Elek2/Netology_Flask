import requests, json

def user_get():
    headers = {}
    response = requests.get("http://127.0.0.1:5000/adv/", headers=headers)
    print(response.text)


def user_post():
    headers = {'Content-Type': 'application/json'}
    data = {
        'username': 'sdgsdg',
        'password': '222',
    }
    json_data = json.dumps(data)
    response = requests.post("http://127.0.0.1:5000/user/", headers=headers, data=json_data)
    print(response.text)


user_get()