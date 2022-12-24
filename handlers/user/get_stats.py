from aiogram import types
from aiogram.dispatcher import FSMContext

from db import database

async def get_stats(msg: types.Message, state: FSMContext):
    count = await database.get_count(msg.from_user.id)
    await msg.answer(f"количество отправленных сообщений: {count}")
