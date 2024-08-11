from aiogram.fsm.state import StatesGroup, State


class States(StatesGroup):
    # Админ
    admin = State()

    on_start = State()
    demo = State()
    end = State()
