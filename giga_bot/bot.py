from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from db import database

async def on_startup(dp: Dispatcher):
    import handlers
    handlers.user.setup(dp)

if __name__ == "__main__":
    bot = Bot(token=config.BOT_TOKEN, validate_token=True)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
