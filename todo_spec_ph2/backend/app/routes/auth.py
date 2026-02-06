from fastapi import APIRouter, HTTPException, status

from ..models.auth import AuthRequest, AuthResponse
from ..services.auth import issue_token

router = APIRouter(prefix="/auth", tags=["auth"])


def _bad_request(exc: ValueError) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=str(exc) or "Invalid request",
    )


@router.post("/signup", response_model=AuthResponse)
def signup(payload: AuthRequest) -> AuthResponse:
    try:
        token, user_id = issue_token(payload.email, payload.password)
    except ValueError as exc:
        raise _bad_request(exc)
    return AuthResponse(token=token, user_id=user_id)


@router.post("/login", response_model=AuthResponse)
def login(payload: AuthRequest) -> AuthResponse:
    try:
        token, user_id = issue_token(payload.email, payload.password)
    except ValueError as exc:
        raise _bad_request(exc)
    return AuthResponse(token=token, user_id=user_id)
