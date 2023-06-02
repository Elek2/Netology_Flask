import json

from flask import Flask, jsonify, request, g
from flask.views import MethodView

from auth import basic_auth
from hash import hash_password
from models import Advertisement, Session, User

app = Flask(__name__)


@app.route('/')
def check_ok():
    return 'Flask is running'


class UserClass(MethodView):

    def get(self, ):
        with Session() as s:
            users = s.query(User).filter_by(**request.args)

            user_list = []
            for user in users:
                user_data = dict()
                user_data['id'] = user.id
                user_data['name'] = user.username
                user_data['password'] = user.password
                user_list.append(user_data)

            return json.dumps(jsonify(user_list).json, indent=2)

    def post(self, **kwargs):
        with Session() as s:
            new_user = User(**request.json)
            new_user.password = hash_password(new_user.password)
            s.add(new_user)
            s.commit()

            user_data = dict()
            user_data['id'] = new_user.id
            user_data['name'] = new_user.username
            user_data['email'] = new_user.email
            user_data['password'] = new_user.password
            return user_data


class AdvertClass(MethodView):
    @staticmethod
    def get():
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

            return json.dumps(jsonify(adv_list).json, indent=2)

    @basic_auth.login_required
    def post(self):
        with Session() as s:
            new_adv = Advertisement(**request.json)
            new_adv.author_id = g.current_user.id

            s.add(new_adv)
            s.commit()

            adv_data = dict()
            adv_data['header'] = new_adv.header
            adv_data['description'] = new_adv.description
            adv_data['created_on'] = new_adv.created_on
            adv_data['owner'] = new_adv.users.username
            return adv_data

    def delete(self, adv_id):
        with Session() as s:
            delete_adv = s.query(Advertisement).get(adv_id)
            s.delete(delete_adv)
            s.commit()
            return 'ok'


adv_view = AdvertClass.as_view('adv')

app.add_url_rule('/user/', view_func=UserClass.as_view('user'), methods=['GET', 'POST'])
app.add_url_rule('/adv/<int:adv_id>', view_func=adv_view, methods=['DELETE'])
app.add_url_rule('/adv/', view_func=adv_view, methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run()
