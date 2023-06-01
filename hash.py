import hashlib

SALT = "sada r32r 8#&Y 78"

def hash_password(password):
    password += SALT
    password = password.encode()
    return str(hashlib.md5(password))