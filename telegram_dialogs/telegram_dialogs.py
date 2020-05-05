import os

from telethon import TelegramClient
from telethon.sessions import StringSession

from utils.get_env import api_hash, api_id
from utils.get_message import get_messages
from utils.check_file_exit import exit_files
from utils.create_file import create_filename, create_new_dir

from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from telethon.tl.custom.file import File


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

    try:
        entity = await client.get_entity(PeerUser(chat_id))
    except:
        try:
            entity = await client.get_entity(PeerChannel(chat_id))
        except:
            entity = await client.get_entity(PeerChat(chat_id))

    messages = []

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
            files = File(message.file)

            dirName = f'./Chat/{chat_id}/'
            create_new_dir(dirName)

            filename = create_filename(
                dirName,
                files.media.media.access_hash,
                files.media.mime_type
            )
            if exit_files(dirName, filename, files.media.mime_type):
                with open(filename, 'wb') as fd:
                    async for chunk in client.iter_download(files.media.media):
                        fd.write(chunk)

        user = await client.get_entity(message.from_id)
        message = get_messages(message, user.username, media=filename)
        messages.append(message)

    return messages


# 5ea28612fc329b4980f45c39
