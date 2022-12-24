from aiogram import types
from aiogram.dispatcher import FSMContext

from db import database

async def top(msg: types.Message, state: FSMContext):
    top = await database.get_top()
    answer = "топовые отправители рандомных сообщений:\n" + "\n".join(["{}: {} сообщений".format(nickname, count) for nickname, count in top])
    await msg.answer(answer)
