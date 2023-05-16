from aiogram import types, Dispatcher
from bot_creating import bot, BAD_FILTER
import json

# @dp.message_handler()
async def echo_simplecommands(message : types.Message):
    
    if {i.lower().translate(str.maketrans('', '', BAD_FILTER + '№')) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('bads.json')).split(' '))) != set():
        await message.answer('Bad words restricted! Thats enough 🤬')
        await message.delete()
    elif message.text.upper() in ('HI', 'BYE', 'LINK'):
        match message.text.upper():
            case 'HI':
                await message.answer('Oh, hi, who are you?')
            case 'BYE':
                await message.answer('Fine, farewell :(')
            case 'LINK':
                await message.answer('Im here, bro')
    else:
        pass
        # await bot.send_message(message.from_user.id, 'This command doesnt exits')
        # await message.delete()

def register_handlers_other(dp: Dispatcher):

    dp.register_message_handler(echo_simplecommands)
    # dp.register_message_handler(command_notexisting)