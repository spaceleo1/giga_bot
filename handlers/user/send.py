from aiogram import types
from aiogram.dispatcher import FSMContext

import states.user

async def send(msg: types.Message, state: FSMContext):
    await states.user.SendMessage.typing_message.set()
    await msg.answer(f"введи сообщение и оно отправится рандомному пользователю😈")
