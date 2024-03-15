from asyncio import sleep
from typing import AsyncGenerator, cast

from pyrogram import filters
from pyrogram.client import Client
from pyrogram.types import Chat, Message

from gigyzer.app import botClient, userClient
from gigyzer.database import UserSchema, create_user, get_user
from gigyzer.utils import Gigachat


@botClient.on_message(filters.command("start"))
async def start_command_handler(client: Client, message: Message):
    old_user = get_user({"user_id": message.from_user.id})
    if not old_user:
        create_user(UserSchema(
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            username=message.from_user.username,
            user_id=message.from_user.id,
        ))
    return await message.reply("Gigyzer is a telegram bot based on the Giga Chat neural network from Sberbank for analyzing groups and channels, forming and grouping data into a more concise representation")


@botClient.on_message(filters.command(["question", "q"]))
async def question_command_handler(client: Client, message: Message):
    units = message.text.split(" ")
    try:
        question = " ".join(units[1:])
        completion = await Gigachat.completion(question) or ""
        return await message.reply(completion)
    except Exception as e:
        print(f"Error: {e}")
        return


@botClient.on_message(filters.command(["analyze", "a"]))
async def analyze_command_handler(client: Client, message: Message):
    try:
        units = message.text.split(" ")
        _, chat_id, *question = units
        if (not chat_id):
            return await message.reply("Chat id is required")
        for _ in range(2):
            chat = await userClient.get_chat(chat_id)
            if isinstance(chat, Chat):
                chat_history = cast(AsyncGenerator[Message, None] | None,
                                    userClient.get_chat_history(chat.id, limit=20))
                if not chat_history:
                    return await message.reply("It was not possible to collect enough data from the chat for analysis and subsequent response")
                messages = []
                async for m in chat_history:
                    m_args = m.text or m.caption
                    if m_args:
                        messages.append(m_args)
                user_content = " ".join(messages)
                system_content = " ".join(question)
                completion = await Gigachat.completion(user_content, system_content)
                if completion:
                    return await message.reply(completion)
                else:
                    return await message.reply("Sorry, I`am don`t know ..")
            else:
                await userClient.join_chat(chat_id)
                await sleep(5)
        return await message.reply("It was not possible to log in to the chat to get information, perhaps the administrator still allowed you to log in, try later")
    except Exception as e:
        print(f"Error: {e}")
        return


__all__ = ["start_command_handler", "question_command_handler", "analyze_command_handler"]
