import os
from aiogram import types, Dispatcher
from aiogram.utils import exceptions as tgExceptions
from bot_creating import bot
from keybuttons import kb_client
from keybuttons.inline_keys import inline_client
from aiogram.dispatcher.filters import Text
from database import sqlite_db

greeting_message = '''
🦧 Добро пожаловать на планету FUFO. 🦧
На данный момент планета развивается и пополняется новыми жителями.
Вы можете создать свое племя и пополнить его четырьмя персонажами.
В дальнейшем (неизвестно когда) ваше племя сможет взаимодействовать в другими.
'''



# @dp.message_handler(commands=COMMANDS)
async def commands_start(message: types.Message):
    try:
        
        await message.answer(greeting_message, reply_markup=inline_client)
        
        # await message.delete()
            
    except tgExceptions.BotBlocked:
        await message.reply(f"Add me please, so i cant type to you in private: {os.getenv('botLink')}")

async def command_fufo(message: types.Message):
    await message.answer('This is FUFO group. Make your character alive', reply_markup=inline_client)

async def command_characters(callback: types.CallbackQuery):
    await sqlite_db.sql_read_command(callback)
    await callback.answer()
    

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands='start')
    # dp.register_message_handler(commands_info, commands='info')
    # dp.register_message_handler(commands_say, commands='say')
    dp.register_message_handler(command_fufo, lambda message: 'фуф' in (message.text).lower())
    dp.register_callback_query_handler(command_characters, Text('characters'))
    # dp.register_message_handler(command_notexisting)

