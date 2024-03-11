from pyrogram import Client
from pyrogram.types import Message

from gigyzer import userClient
from gigyzer.utils import Gigachat


async def start_command(client: Client, message: Message):
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


__all__ = ['start_command', 'analyze_command']
