import base64
import hashlib
import hmac
import json
import time
from typing import Any

from ..config import require_env


def _b64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode("utf-8").rstrip("=")


def _get_secret() -> bytes:
    return require_env("BETTER_AUTH_SECRET").encode("utf-8")


def _encode_segment(payload: dict[str, Any]) -> str:
    encoded = json.dumps(payload, separators=(",", ":")).encode("utf-8")
    return _b64url_encode(encoded)


def create_token(user_id: str, email: str | None = None) -> str:
    header = {"alg": "HS256", "typ": "JWT"}
    payload: dict[str, Any] = {
        "sub": user_id,
        "iat": int(time.time()),
    }
    if email:
        payload["email"] = email

    header_segment = _encode_segment(header)
    payload_segment = _encode_segment(payload)
    signing_input = f"{header_segment}.{payload_segment}".encode("utf-8")
    signature = hmac.new(_get_secret(), signing_input, hashlib.sha256).digest()
    signature_segment = _b64url_encode(signature)
    return f"{header_segment}.{payload_segment}.{signature_segment}"
