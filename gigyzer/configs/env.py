from os import getenv
from pathlib import Path, PurePath

from dotenv import load_dotenv

load_dotenv()

APP_PATH = Path(__file__).resolve().parent.parent.parent
NODE = "prod" if getenv(key="NODE") == "" else ".dev"

load_dotenv(dotenv_path=PurePath(APP_PATH, ".env" + NODE))

TELEGRAM_APP_API_ID = getenv(key="TELEGRAM_APP_API_ID")
TELEGRAM_APP_API_HASH = getenv(key="TELEGRAM_APP_API_HASH")
TELEGRAM_APP_API_SESSION = getenv(key="TELEGRAM_APP_API_SESSION")
TELEGRAM_BOT_API_TOKEN = getenv(key="TELEGRAM_BOT_API_TOKEN")
GIGACHAT_APP_API_ID = getenv(key="GIGACHAT_APP_API_ID")
GIGACHAT_APP_API_SECRET = getenv(key="GIGACHAT_APP_API_SECRET")
GIGACHAT_APP_API_AUTH = getenv(key="GIGACHAT_APP_API_AUTH")
GIGACHAT_APP_API_SCOPE = getenv(key="GIGACHAT_APP_API_SCOPE")


__all__ = [
    "APP_PATH",
    "NODE",
    "TELEGRAM_APP_API_ID",
    "TELEGRAM_APP_API_HASH",
    "TELEGRAM_APP_API_SESSION",
    "TELEGRAM_BOT_API_TOKEN",
    "GIGACHAT_APP_API_ID",
    "GIGACHAT_APP_API_SECRET",
    "GIGACHAT_APP_API_AUTH",
    "GIGACHAT_APP_API_SCOPE",
]
