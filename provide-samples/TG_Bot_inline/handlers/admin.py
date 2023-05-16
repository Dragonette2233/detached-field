from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from bot_creating import dp, bot
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from database import sqlite_db
from keybuttons import admin_keys, client_keys, inline_keys

ID = None
EDITOR_MESSAGE = '''
Вы вошли в редактор персонажей.
Возможные действия представлены ниже
🦍 Слава FUFO 🦍
'''

class FSMAdmin(StatesGroup):
    user_id = State()
    photo = State() # фотография персонажа
    name = State() # имя персонажа
    residence = State() # место проживания (может быть вымышленный город)
    nature = State() # характер персонажа


'''Entry into admin state'''
async def make_changes_command(callback: types.CallbackQuery, state: FSMContext):
    # global ID
    # ID = message.from_user.id
    print(callback.from_user.id)
    await bot.send_message(callback.from_user.id, EDITOR_MESSAGE, reply_markup=(inline_keys.inline_editor))
    await FSMAdmin.user_id.set()
    async with state.proxy() as data:
        data['user_id'] = callback.from_user.id
    await callback.answer()
    # await FSMAdmin.next()
    # await message.delete()

'''Out of admin state'''
async def cancle_handler(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
    await bot.send_message(callback.from_user.id, '🟠 Режим создания закрыт')
    # await callback.delete()

# @dp.message_handler(commands='Load', state=None)
async def charmake_create(callback: types.CallbackQuery):
    # if message.from_user.id == ID:
    idcheck = await sqlite_db.sql_lookfor_userid(callback)
    if idcheck is None:
        # await FSMAdmin.photo.set()
        await bot.send_message(callback.from_user.id, 'Загрузите фото персонажа')
        await FSMAdmin.next()
    else:
        await callback.answer('Вы не можете создать персонажа повторно.')


# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_id'] = message.from_user.id
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply('Введите имя персонажа')

# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply('Введите название местности проживания (Может быть вымышленным, не более 20 символов)')

# @dp.message_handler(state=FSMAdmin.residence)
async def load_residence(message: types.Message, state: FSMContext):
    if len(message.text) < 21:
        async with state.proxy() as data:
            data['residence'] = message.text
        await FSMAdmin.next()
        await message.reply('Опишите характер персонажа (Не больше 80 символов)')
    else:
        await message.reply('🟡 Название местности должно содержать не более 20 символов. Попробуйте еще раз')

# @dp.message_handler(state=FSMAdmin.nature)
async def load_nature(message: types.Message, state: FSMContext):
    if len(message.text) < 81:
        async with state.proxy() as data:
            data['nature'] = message.text
        
        await sqlite_db.sql_add_command(state)

        await bot.send_message(message.from_user.id, '🟢 Создание заверешено!', reply_markup=client_keys.kb_client)
        # print(data)
        await state.finish()
    else:
        await message.reply('🟡 Характер персонажа должен содержать не более 80 символов. Попробуйте еще раз')

async def charmake_delete(callback: types.CallbackQuery):
    idcheck = await sqlite_db.sql_lookfor_userid(callback)
    if idcheck:
        await bot.send_message(callback.from_user.id, 'Вы действительно хотите удалить своего персонажа?', reply_markup=inline_keys.inline_yesno)
    else:
        await bot.send_message(callback.from_user.id, 'У вас нет активного персонажа. Но никогда не поздно его воссоздать')
    

async def charmake_delete_yesno(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'yes_delete':
        await sqlite_db.sql_delete_command(callback)
        await bot.send_message(callback.from_user.id, 'Ваш фуфо ушел на покой... 😔')
        await state.finish()
        await callback.answer()
    else:
        await bot.send_message(callback.from_user.id, 'Вы сохранили жизнь вашему фуфо')
        await callback.answer()
            
def register_handlers_admin(dp: Dispatcher):
    '''Вход в редактор персонажа'''
    dp.register_callback_query_handler(make_changes_command, Text('editor'), state=None)
    '''Создание персонажа'''
    dp.register_callback_query_handler(charmake_create, Text('create'), state=FSMAdmin.user_id)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_residence, state=FSMAdmin.residence)
    dp.register_message_handler(load_nature, state=FSMAdmin.nature)
    '''Удаление персонажа'''
    dp.register_callback_query_handler(charmake_delete, Text('delete'), state='*')
    dp.register_callback_query_handler(charmake_delete_yesno, Text(endswith='_delete'), state='*')
    '''Выход из состояние FSM'''
    dp.register_callback_query_handler(cancle_handler, Text('cancel'), state='*')
    # dp.register_message_handler(cancle_handler, Text(equals='abort', ignore_case=True), state='*')
    

