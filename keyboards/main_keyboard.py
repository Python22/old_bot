from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import KeyboardButton, InlineKeyboardButton, ReplyKeyboardBuilder


def generate_row_keyboard(items: list["str"]) -> ReplyKeyboardMarkup:
    """
    :param items: ["aaa", "bbb"]
    keyboard = [KeyboardButton(text="aaa"), KeyboardButton(text="bbb")]
    :return:
    """
    keyboard = [KeyboardButton(text=elem) for elem in items]
    return ReplyKeyboardMarkup(keyboard=[keyboard], resize_keyboard=True)

