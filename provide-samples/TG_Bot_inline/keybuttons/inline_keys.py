from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

INLINE_BUTTONS = (
    InlineKeyboardButton(text='Редактор', callback_data='editor'),
    InlineKeyboardButton(text='Мои персонажи', callback_data='characters')
)

EDITOR_BUTTONS = (
    InlineKeyboardButton(text='Создать', callback_data='create'),
    InlineKeyboardButton(text='Изменить', callback_data='edit'),
    InlineKeyboardButton(text='Удалить', callback_data='delete'),
    InlineKeyboardButton(text='Отмена', callback_data='cancel')
)

YESNO_BUTTONS = (
    InlineKeyboardButton(text='Да', callback_data='yes_delete'),
    InlineKeyboardButton(text='Нет', callback_data='no_delete')
)

inline_client = InlineKeyboardMarkup(row_width=2).add(*INLINE_BUTTONS)
inline_editor = InlineKeyboardMarkup(row_width=3).row(*EDITOR_BUTTONS[0:3]).add(EDITOR_BUTTONS[3])
inline_yesno = InlineKeyboardMarkup(row_width=2).row(*YESNO_BUTTONS)