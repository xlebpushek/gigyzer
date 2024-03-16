from asyncio import get_event_loop

from pyrogram.sync import compose

from gigyzer.app import botClient, userClient


async def bootstrap():
    await compose([botClient, userClient])

if __name__ == "__main__":
    loop = get_event_loop()
    loop.run_until_complete(bootstrap())
