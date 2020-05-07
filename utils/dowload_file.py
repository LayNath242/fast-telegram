from telethon.tl.custom.file import File

from utils._file import create_filename, create_new_dir, exit_files, create_profile_name
from utils.get_entity import get_entity


async def download_file(media, chat_id, client):
    files = File(media)

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
    return filename


async def download_profile(chat_id, photo, client, big=False):
    entity = await get_entity(chat_id, client)

    dirname = f'./Chat/{chat_id}/'

    try:
        filename = create_profile_name(dirname, photo.photo_id, big)
    except:
        filename = None
    await client.download_profile_photo(entity, file=filename, download_big=big)

    return filename
