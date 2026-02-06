from sqlmodel import Session, create_engine

from ..config import require_env

_engine = None


def get_engine():
    global _engine
    if _engine is None:
        database_url = require_env("DATABASE_URL")
        _engine = create_engine(database_url, echo=False, pool_pre_ping=True)
    return _engine


def get_session():
    engine = get_engine()
    with Session(engine) as session:
        yield session
