from typing import List
from datetime import datetime, date

from fastapi import APIRouter, Depends, HTTPException

from database.mongodb import db
from utils.get_telegram import _get_telegram_or_404

from .telegram_dialogs import get_all_dialogs, get_all_messages, \
    send_message, upload_file

telegramDialogs_router = APIRouter()


@telegramDialogs_router.get("/get_all_dialogs")
async def get_dialogs(id: str, limit: int = 10):
    auth = await _get_telegram_or_404(id)
    dialogs = await get_all_dialogs(auth['auth_key'], limit)
    return {'data': dialogs}


@telegramDialogs_router.get("/get_all_messages")
async def get_messages(id: str,
                       chat_id: int,
                       limit: int = 10,
                       search: str = None,
                       reverse: bool = False,
                       offset_date: date = None,
                       ids: int = None,
                       from_user: int = None,
                       ):
    auth = await _get_telegram_or_404(id)
    messages = await get_all_messages(
        auth['auth_key'],
        chat_id,
        limit,
        search,
        reverse,
        offset_date,
        ids,
        from_user
    )

    return {'data': messages}


@telegramDialogs_router.get("/send_messages")
async def sendMessages(
    message: str,
    reply_to: int = None,
    parse_mode: str = None,
    link_preview: bool = True,
    clear_draft: bool = False,
    silent: bool = False,
    schedule: datetime = None,
    chat_id: int = 1266629372,
    id: str = '5ea28612fc329b4980f45c39',
):
    auth = await _get_telegram_or_404(id)

    messages = await send_message(
        auth['auth_key'],
        chat_id,
        message,
        reply_to,
        parse_mode,
        link_preview,
        clear_draft,
        silent,
        schedule,
    )

    return {'data': messages}


@telegramDialogs_router.post("/upload_file")
async def uploadFile(
    file: List[str],
    caption: str = None,
    thumb: str = None,
    chat_id: int = 1266629372,
    id: str = '5ea28612fc329b4980f45c39',
):
    auth = await _get_telegram_or_404(id)

    file = await upload_file(
        auth['auth_key'],
        chat_id,
        file,
        caption,
        thumb
    )
    if file:
        return {'data': 'upload success'}

    return {'data': 'upload fail'}
