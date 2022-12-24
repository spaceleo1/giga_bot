from aiogram import types
from aiogram.dispatcher import FSMContext

async def help(msg: types.Message, state: FSMContext):
    await msg.answer('''
/start -- стартовать/поменять ник
/help -- открыть данное меню
/send -- отправить сообщение рандомному пользователю
/get_stats -- посмотреть сколько сообщений ты отправил
/get_nickname -- посмотреть свой текущий никнейм
/top -- посмотреть топ клоунов''')
