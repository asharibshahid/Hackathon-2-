import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value

DATABASE_URL = require_env("DATABASE_URL")
BETTER_AUTH_SECRET = require_env("BETTER_AUTH_SECRET")
OPENAI_API_KEY = require_env("OPENAI_API_KEY")