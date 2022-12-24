from aiogram.dispatcher.filters.state import State, StatesGroup

class Register(StatesGroup):
    register = State()

class SendMessage(StatesGroup):
    typing_message = State()