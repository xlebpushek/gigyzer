from pyrogram import compose, filters
from pyrogram.handlers import MessageHandler

from gigyzer import botClient, userClient
from gigyzer.handlers.commands import analyze_command, start_command

botClient.add_handler(MessageHandler(
    start_command,
    filters.command('start'))
)
botClient.add_handler(MessageHandler(
    analyze_command,
    filters.command('qu'))
)


async def bootstrap():
    await compose([botClient, userClient])


__all__ = ['botClient', 'userClient', 'bootstrap']
