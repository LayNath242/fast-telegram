from telethon.tl.types import PeerUser, PeerChat, PeerChannel


async def get_entity(chat_id, client):
    try:
        entity = await client.get_entity(PeerUser(chat_id))
    except:
        try:
            entity = await client.get_entity(PeerChannel(chat_id))
        except:
            entity = await client.get_entity(PeerChat(chat_id))
    return entity
