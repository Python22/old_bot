from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove
from keyboards.main_keyboard import generate_row_keyboard
from states_and_data import pizza_names, pizza_sizes, UserStates
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


router = Router()


@router.message(UserStates.user_pizza_name, F.text.lower().in_(pizza_names))
async def choose_name(message: Message, state: FSMContext):
    await state.update_data(user_pizza_name=message.text.lower())
    await message.answer(f"Ваш выбор - {str(message.text.lower())} ")
    await message.answer(
        text="Выберите размер пиццы: ",
        reply_markup=generate_row_keyboard(pizza_sizes)
    )
    await state.set_state(UserStates.user_pizza_size)


@router.message(UserStates.user_pizza_size, F.text.lower().in_(pizza_sizes))
async def choose_size(message: Message, state: FSMContext):
    await state.update_data(user_pizza_size=message.text.lower())
    await message.answer(f"Ваш выбор - {str(message.text.lower())} ")
    user_data = await state.get_data()

    await message.answer(
        text=f"Спасибо за заказ! Ваш заказ: {user_data['user_pizza_name']} - {user_data['user_pizza_size']}",
        reply_markup=ReplyKeyboardRemove()
    )
    print(message.from_user.id)
    # with open("data.txt", "w", encoding="utf-8") as file:
    #     file.write(f"{str(message.from_user.id)}: {user_data['user_pizza_name']}; {user_data['user_pizza_size']};")
    await state.clear()
