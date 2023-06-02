import hashlib
import os

from flask import g
from flask_httpauth import HTTPBasicAuth

from models import Session, User

basic_auth = HTTPBasicAuth()


def hash_password(password):
    password += os.getenv("USER_PASSWORD_SALT")
    password = password.encode()
    return hashlib.md5(password).hexdigest()


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
