import base64
import hashlib
import hmac
import json
from typing import Any

from fastapi import Header, HTTPException, status

from ..config import require_env


def _b64url_decode(segment: str) -> bytes:
    padding = "=" * (-len(segment) % 4)
    return base64.urlsafe_b64decode(segment + padding)


def _decode_json(segment: str) -> dict[str, Any]:
    try:
        raw = _b64url_decode(segment)
        return json.loads(raw.decode("utf-8"))
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        ) from exc


def _get_secret() -> str:
    try:
        return require_env("BETTER_AUTH_SECRET")
    except RuntimeError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Server configuration error",
        ) from exc


def _verify_hs256(header_segment: str, payload_segment: str, signature_segment: str) -> dict[str, Any]:
    header = _decode_json(header_segment)
    if header.get("alg") != "HS256":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

    secret = _get_secret().encode("utf-8")
    signing_input = f"{header_segment}.{payload_segment}".encode("utf-8")
    expected = hmac.new(secret, signing_input, hashlib.sha256).digest()
    try:
        actual = _b64url_decode(signature_segment)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        ) from exc

    if not hmac.compare_digest(expected, actual):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

    return _decode_json(payload_segment)


def _extract_bearer_token(authorization: str | None) -> str:
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing Authorization header",
        )

    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer" or not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Authorization header",
        )
    return token


def _get_token_identity(payload: dict[str, Any]) -> str:
    user_id = payload.get("sub") or payload.get("email")
    if not user_id or not isinstance(user_id, str):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
    return user_id


def require_authenticated_user(
    user_id: str,
    authorization: str | None = Header(default=None, convert_underscores=False),
) -> str:
    token = _extract_bearer_token(authorization)
    parts = token.split(".")
    if len(parts) != 3:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

    payload = _verify_hs256(parts[0], parts[1], parts[2])
    token_user_id = _get_token_identity(payload)

    if token_user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User mismatch",
        )

    return token_user_id
