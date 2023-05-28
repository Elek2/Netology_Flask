import requests


def requets_test():
    response = requests.get("http://127.0.0.1:5000/")
    print(response.json())
    return response

requets_test()