import hashlib

SALT = "sAda r32r 8#&Y 78"

def hash_password(password):
    password += SALT
    password = password.encode()
    return hashlib.md5(password).hexdigest()

def check_password(password):
    return hash_password()