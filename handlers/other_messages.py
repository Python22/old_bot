from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup
from keyboards.main_keyboard import generate_row_keyboard
from states_and_data import pizza_names, pizza_sizes, UserStates
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


router = Router()


@router.message(Command("start"))       # /start
async def start(message: Message, state: FSMContext):

    await message.answer(
        text="Выберите название пиццы: ",
        reply_markup=generate_row_keyboard(pizza_names)
    )
    await state.set_state(UserStates.user_pizza_name)
