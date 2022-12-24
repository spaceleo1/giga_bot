from aiogram import types
from aiogram.dispatcher import FSMContext

from db import database 

async def type_message(msg: types.Message, state: FSMContext):
    await state.finish()

    user_id = await database.get_random()
    await database.inc_count(msg.from_user.id)
    cur_nickname = await database.get_nickname(msg.from_user.id)

    await msg.bot.send_message(user_id, f"пользователь {cur_nickname} отправил тебе сообщение😈😈😈:")
    await msg.bot.send_message(user_id, msg.text)
    await msg.answer(f"поздры ты успешно отправил сообщение")
