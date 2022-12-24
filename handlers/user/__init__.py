from aiogram import Dispatcher
from aiogram.dispatcher.filters import Command, CommandStart, CommandHelp, Text

import states.user
from .start import bot_start
from .register import register
from .send import send
from .type_message import type_message
from .get_stats import get_stats
from .get_nickname import get_nickname
from .help import help
from .top import top

def setup(dp: Dispatcher):
    dp.register_message_handler(bot_start, CommandStart(), state="*")
    dp.register_message_handler(register, Text(startswith=""), state=states.user.Register.register)
    dp.register_message_handler(send, Command("send"), state="*")
    dp.register_message_handler(type_message, Text(startswith=""), state=states.user.SendMessage.typing_message)
    dp.register_message_handler(get_stats, Command("get_stats"), state="*")
    dp.register_message_handler(get_nickname, Command("get_nickname"), state="*")
    dp.register_message_handler(help, CommandHelp(), state="*")
    dp.register_message_handler(top, Command("top"), state="*")