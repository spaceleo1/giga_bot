from aiogram import types
from aiogram.dispatcher import FSMContext

from db import database

async def get_nickname(msg: types.Message, state: FSMContext):
    nickname = await database.get_nickname(msg.from_user.id)
    await msg.answer(f"твой текущий никнейм: {nickname}\nпоменять его можно командой /start")
