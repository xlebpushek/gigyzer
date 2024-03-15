from pyrogram import Client
from pyrogram.types import Message

from gigyzer.app import userClient
from gigyzer.database import create_user, get_user, schemas
from gigyzer.utils import Gigachat


async def start_command(client: Client, message: Message):
    create_user(schemas.UserModel(
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
        username=message.from_user.username,
        user_id=message.from_user.id,
    ))
    return await message.reply("Hello, I'm Gigyzer bot. I can analyze information from channels and groups to give a general answer to your question")


async def analyze_command(client: Client, message: Message):
    units = message.text.split(' ')
    chat_tag = units[1]
    if (not chat_tag):
        return await message.reply("Chat tag is required")
    try:
        chat = await userClient.get_chat(chat_tag)
        messages = []
        async for m in userClient.get_chat_history(chat.id, limit=20):
            if (m.text or m.caption):
                messages.append(m.text or m.caption)
        context = ' '.join(messages)
        question = ' '.join(units[2:])
        completion = await Gigachat.completion(context, question)
        return await message.reply(completion)
    except Exception as e:
        print(f"Error: {e}")
        return


__all__ = ['start_command', 'get_user_command', 'analyze_command']
