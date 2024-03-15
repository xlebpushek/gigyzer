from pyrogram import Client

from gigyzer.configs import (TELEGRAM_APP_API_HASH, TELEGRAM_APP_API_ID,
                             TELEGRAM_BOT_API_TOKEN)

botClient = Client(
    'bot',
    api_id=TELEGRAM_APP_API_ID,
    api_hash=TELEGRAM_APP_API_HASH,
    bot_token=TELEGRAM_BOT_API_TOKEN
)
userClient = Client(
    'client',
    api_id=TELEGRAM_APP_API_ID,
    api_hash=TELEGRAM_APP_API_HASH
)


__all__ = ['botClient', 'userClient']
