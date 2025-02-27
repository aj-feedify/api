import jwt
import datetime
import os
from dotenv import load_dotenv
from typing import Any

load_dotenv()


def generate_jwt(text: Any) -> str:
    expiration = datetime.datetime.utcnow() + datetime.timedelta(days=10 * 365)
    payload = {
        "sub": text,
        "exp": expiration,
    }
    token = jwt.encode(payload, os.environ.get("JWT_SECRET_KEY"), algorithm="HS256")

    return token
