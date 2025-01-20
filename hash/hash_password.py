import hashlib


def hash_password(password: str) -> str:
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed
