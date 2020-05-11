import os

from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.users import GetFullUserRequest


from utils.get_env import api_hash, api_id
from utils.get_message import get_messages
from utils.dowload_file import download_file, download_profile_photo
from utils.get_entity import get_entity
from utils._file import create_new_dir


async def get_all_dialogs(
        auth_key,
        limit
):
    client = TelegramClient(StringSession(auth_key), api_id, api_hash)
    await client.connect()

    data = []

    async for dialog in client.iter_dialogs(limit=limit):

        entity = await get_entity(dialog.entity.id, client)
        # dirname = f"Chat/{dialog.entity.id}/"
        # create_new_dir(dirname)
        # filename = f"{dirname}profile/{dialog.name}"
        # file = await client.download_profile_photo(entity, file=filename, download_big=False)
        filename = await download_profile_photo(entity, client, dialog.entity.id, dialog.name)
        user = dialog.message
        if user.media:
            try:
                if user.media.photo:
                    message = "photo"
                else:
                    message = "unknow"
            except:
                try:
                    _type = str(user.media.document.mime_type)
                    if _type == "image/webp":
                        message = "sticker"
                    elif _type == "audio/ogg":
                        message = "voice message"
                    elif _type.split("/")[0] == "audio":
                        message = "audio"
                    elif _type.split("/")[0] == "video":
                        message = "video"
                    else:
                        message = "media"
                except:
                    message = "unknow"
        else:
            message = user.message
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
