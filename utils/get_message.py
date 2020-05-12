
def get_messages(message, username, media):
    datas = []
    data = {
        'message_id': message.id,
        'from_user': username,
        'message': message.text,
        'date': message.date,
        'media': media,
        'reply_to_msg_id': message.reply_to_msg_id
    }
    datas.append(data)
    return data


async def get_lastest_message(user, client, entity):
    if user.geo:
        message = str(user.geo)

    elif user.venue:
        message = str(user.venue)

    elif user.invoice:
        message = str(user.invoice)

    elif user.poll:
        message = str(user.poll)

    elif user.web_preview:
        message = user.message

    elif user.contact:
        message = "contact"

    elif user.game:
        message = "game"

    elif user.sticker:
        alt = (user.sticker.attributes)[1].alt
        message = f"{alt} sticker"

    elif user.gif:
        message = "GIF"

    elif user.photo:
        message = "photo"

    elif user.video_note or user.video:
        message = "video"

    elif user.voice:
        message = "voice message"

    elif user.is_reply:
        msg_reply = await client.get_messages(entity, ids=user.reply_to_msg_id)
        message = {"reply_msg_to": msg_reply.message, "msg": user.text}

    elif user.text or user.raw_text:
        message = user.text
    else:
        message = "unknow action yet"

    return message
