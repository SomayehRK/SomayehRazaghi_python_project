import hashlib


def hash_pass(password):
    """
    :param password: the password entered user
    :return: Receives the password entered user as the input argument and hashes it.
    """
    password_encode = str(password).encode()
    hash_password = hashlib.md5(password_encode).hexdigest()
    return hash_password
