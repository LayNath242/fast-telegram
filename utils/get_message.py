
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

# get lastest_message()
