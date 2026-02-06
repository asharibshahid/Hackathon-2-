from ..auth.jwt import create_token


def _normalize(value: str | None, label: str) -> str:
    if value is None:
        raise ValueError(f"{label} is required")
    trimmed = value.strip()
    if not trimmed:
        raise ValueError(f"{label} is required")
    return trimmed


def issue_token(email: str | None, password: str | None) -> tuple[str, str]:
    user_id = _normalize(email, "Email")
    _normalize(password, "Password")
    token = create_token(user_id, email=user_id)
    return token, user_id
