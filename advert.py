import json

import requests
from flask import Flask, jsonify, request
from flask.views import MethodView

from models import Session, User, Advertisement


app = Flask(__name__)


@app.route('/')
def check_ok():
    return 'Flask is running'


class UserClass(MethodView):

    def get(self):
        with Session() as s:
            users = s.query(User).all()

            user_list = []
            for user in users:
                user_data = dict()
                user_data['id'] = user.id
                user_data['name'] = user.username
                user_data['date'] = user.created_on
                user_list.append(user_data)

            return user_list

    def post(self, **kwargs):
        with Session() as s:
            new_user = User(**request.json)
            s.add(new_user)
            s.commit()

            user_data = dict()
            user_data['id'] = new_user.id
            user_data['name'] = new_user.username
            user_data['password'] = new_user.password
            return user_data

    def delete(self):
        pass


class AdvertClass(MethodView):

    def get(self):
        with Session() as s:
            advs = s.query(Advertisement).all()

            adv_list = []
            for adv in advs:
                adv_data = dict()
                adv_data['header'] = adv.header
                adv_data['description'] = adv.description
                adv_data['created_on'] = adv.created_on
                adv_data['owner'] = adv.users.username
                adv_list.append(adv_data)

            return adv_list

    def post(self, **kwargs):
        with Session() as s:
            new_user = User(**request.json)
            s.add(new_user)
            s.commit()

            user_data = dict()
            user_data['id'] = new_user.id
            user_data['name'] = new_user.username
            user_data['password'] = new_user.password
            return user_data

    def delete(self):
        pass



app.add_url_rule('/user/', view_func=UserClass.as_view('user'), methods=['GET', 'POST'])
app.add_url_rule('/adv/', view_func=AdvertClass.as_view('adv'), methods=['GET', 'POST'])


if __name__ == '__main__':
    app.run(debug=True)
