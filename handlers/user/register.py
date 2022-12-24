from aiogram import types
from aiogram.dispatcher import FSMContext

from db import database

async def register(msg: types.Message, state: FSMContext):
    await database.save(msg.from_user.id, msg.text)

    await state.finish()
    await msg.answer(
f'''
поздры ты успешно зарегистрирован под именем {msg.text}
чтобы отправить сообщение рандомному пользователю данного офигенного бота набери /send😈
''')
