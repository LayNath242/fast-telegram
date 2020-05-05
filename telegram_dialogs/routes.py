from datetime import datetime, date

from fastapi import APIRouter, Depends, HTTPException

from database.mongodb import db
from utils.get_telegram import _get_telegram_or_404

from .telegram_dialogs import get_all_dialogs, get_all_messages

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
