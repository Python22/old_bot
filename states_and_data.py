from aiogram.fsm.state import State, StatesGroup


class UserStates(StatesGroup):
    user_pizza_name = State()
    user_pizza_size = State()


pizza_names = [
    "пепперони",
    "гавайская",
    "мясная",
    "грибная"
]
pizza_sizes = [
    "маленькая (20 см)",
    "средняя(25 см)",
    "большая (30 см)",
    "гигантская (1 метр)"
]
