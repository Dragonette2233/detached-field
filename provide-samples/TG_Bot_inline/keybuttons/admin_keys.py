from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# Keyboard for admins

btn_load = KeyboardButton('/Создать')
btn_edit = KeyboardButton('/Изменить')
btn_del = KeyboardButton('/Удалить')
btn_cancel = KeyboardButton('/Отмена')

btn_yes = KeyboardButton('/Да')
btn_no = KeyboardButton('/Нет')

btn_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_cancel)
btn_case_yesno = ReplyKeyboardMarkup(resize_keyboard=True).row(btn_yes, btn_no)

