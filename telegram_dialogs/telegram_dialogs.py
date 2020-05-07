import os

from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.users import GetFullUserRequest


from utils.get_env import api_hash, api_id
from utils.get_message import get_messages
from utils.dowload_file import download_file, download_profile
from utils.get_entity import get_entity


async def get_all_dialogs(
        auth_key,
        limit
):
    client = TelegramClient(StringSession(auth_key), api_id, api_hash)
    await client.connect()

    data = []

    async for dialog in client.iter_dialogs(limit=limit):
        user = {
            "id": str(dialog.entity.id),
            "name": dialog.name
        }

        data.append(user)
        filename = await download_profile(dialog.entity.id, dialog.entity.photo, client, big=True)
        print(filename)
    return data


async def get_all_messages(
    auth_key,
    chat_id,
    limit,
    search,
    reverse,
    offset_date,
    ids,
    from_user
):

    client = TelegramClient(StringSession(auth_key), api_id, api_hash)
    await client.connect()

    messages = []

    entity = await get_entity(chat_id, client)

    async for message in client.iter_messages(
            entity,
            limit=limit,
            search=search,
            reverse=reverse,
            offset_date=offset_date,
            ids=ids,
            from_user=from_user
    ):
        filename = None

        if message.media:
            filename = await download_file(message.file, chat_id, client)

        user = await client.get_entity(message.from_id)
        message = get_messages(message, user.username, media=filename)
        messages.append(message)

    return messages

# 5ea28612fc329b4980f45c39
