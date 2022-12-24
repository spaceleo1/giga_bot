from aiogram import types
from aiogram.dispatcher import FSMContext

import states.user

async def bot_start(msg: types.Message, state: FSMContext):
    await states.user.Register.register.set()
    await msg.answer(f"прив введи пж имя под которым тебя будут знать\n"
                      "в любой момент введи /start чтобы ero изменить\n"
                      "чтобы увидеть список возможностей бота введи /help")
