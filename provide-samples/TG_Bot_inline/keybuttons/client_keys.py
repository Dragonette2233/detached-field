from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BUTTONS = (
    KeyboardButton('/start'),
    KeyboardButton('/design'),
    KeyboardButton('/characters')
)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.row(*BUTTONS)

