import os

from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.users import GetFullUserRequest


from utils.get_env import api_hash, api_id
from utils.get_message import get_messages, get_lastest_message
from utils.dowload_file import download_file, download_profile_photo
from utils.get_entity import get_entity
from utils._file import create_new_dir


async def get_all_dialogs(
        auth_key,
        limit
):
    try:
        client = TelegramClient(StringSession(auth_key), api_id, api_hash)
        await client.connect()
    except:
        return "client error"

    data = []

    async for dialog in client.iter_dialogs(limit=limit):
        entity = await get_entity(dialog.entity.id, client)
        filename = await download_profile_photo(entity, client, dialog.entity.id, dialog.name)

        user = dialog.message

        try:
            message = await get_lastest_message(dialog.message, client, entity)
        except:
            message = "can not get message"

        user = {
            "id": str(dialog.entity.id),
            "name": dialog.name,
            "photo": filename,
            "message": message,
        }
        data.append(user)

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
    try:
        client = TelegramClient(StringSession(auth_key), api_id, api_hash)
        await client.connect()
    except:
        return "client error"

    messages = []
    try:
        entity = await get_entity(chat_id, client)
    except:
        return "entity error"

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

