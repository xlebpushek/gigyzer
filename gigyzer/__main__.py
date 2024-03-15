from asyncio import get_event_loop

from pyrogram import compose, filters
from pyrogram.handlers import MessageHandler

from gigyzer.app import botClient, userClient
from gigyzer.handlers import *


async def bootstrap():
    botClient.add_handler(MessageHandler(
        start_command,
        filters.command('start'))
    )

    botClient.add_handler(MessageHandler(
        analyze_command,
        filters.command('qu'))
    )
    await compose([botClient, userClient])

if __name__ == "__main__":
    loop = get_event_loop()
    loop.run_until_complete(bootstrap())
