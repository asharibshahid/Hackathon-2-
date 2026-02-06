from sqlmodel import SQLModel


class AuthRequest(SQLModel):
    email: str | None = None
    password: str | None = None


class AuthResponse(SQLModel):
    token: str
    user_id: str
