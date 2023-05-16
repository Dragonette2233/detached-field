from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text 
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os


bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)
answ = set()

'''url_kb = InlineKeyboardMarkup(row_width=1)
url_btns =(
    InlineKeyboardButton(text='Link [rutracker]', url='https://rutracker.org/forum/index.php'),
    InlineKeyboardButton(text='Link [rargb]', url='https://rargb.to/'),
    InlineKeyboardButton(text='Link [youtube]', url='https://www.youtube.com/feed/subscriptions'),
    InlineKeyboardButton(text='Link [boosty - ikakprosto]', url='https://boosty.to/ikakprosto')
)
url_kb.add(url_btns[0]).row(*url_btns[1:])'''

cb_btn_1 = InlineKeyboardButton(text='Показать кто тут батя', callback_data='1')
# cb_btn_2 = InlineKeyboardButton(text='def -', callback_data='karma -1')
callback_markup = InlineKeyboardMarkup(row_width=2).add(cb_btn_1)


@dp.message_handler(commands='hit')
async def command_url(message: types.Message):
    await message.answer('Действие: ', reply_markup=callback_markup)

@dp.callback_query_handler(Text(startswith='1'))
async def command_answer(callback: types.CallbackQuery):
    # result = int(callback.data.split(' ')[1])
    # print(answ)
    # print(callback.from_user.id)
    if str(callback.from_user.id) not in answ:
        answ.add(f'{callback.from_user.id}')
        await callback.answer('Вы получили в ebich', show_alert=True)
    else:
        await callback.answer('Повторное получение в ebich невозможно')

    # await callback.message.answer('Функция работает исправно')
    # await callback.answer('Inline', show_alert=True)

executor.start_polling(dp, skip_updates=True)