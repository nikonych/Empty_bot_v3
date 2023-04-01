from aiogram.fsm.state import StatesGroup, State


class TokenState(StatesGroup):
    file = State()
    money = State()
    proof = State()

