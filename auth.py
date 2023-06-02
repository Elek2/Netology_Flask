from flask import g
from flask_httpauth import HTTPBasicAuth

from hash import hash_password
from models import User, Session

basic_auth = HTTPBasicAuth()


@basic_auth.verify_password
def verify_password(email, password):
    with Session() as s:
        user = s.query(User).filter_by(email=email).first()
        if user is None:
            return False
        g.current_user = user
    return user.password == hash_password(password)


# https://habr.com/ru/articles/358152/
# https://habr.com/ru/articles/346346/