import sqlite3 as sq
from bot_creating import bot

def sql_start():
    global base, cur
    base = sq.connect('fufo_characters.db')
    cur = base.cursor()
    if base:
        print('Data base of characters connected: 100%')
    base.execute(
        'CREATE TABLE IF NOT EXISTS characters(user_id TEXT PRIMARY KEY, photo TEXT, name TEXT PRIMARY KEY, residense TEXT, nature TEXT)')
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO characters VALUES (?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_read_command(message):
    characters = cur.execute('SELECT * FROM characters').fetchall()
    print(characters)
    if len(characters) != 0:
        for ret in characters:
            await bot.send_photo(message.from_user.id, ret[1], f'Имя: {ret[2]}\nРезиденция: {ret[3]}\nХарактер: {ret[4]}')
    else:
        await bot.send_message(message.from_user.id, 'У вас нет активных персонажей')

async def sql_delete_command(message):
    cur.execute('DELETE FROM characters WHERE user_id == ?', (f'{message.from_user.id}', ))
    base.commit()

async def sql_lookfor_userid(message):
    return cur.execute('SELECT * FROM characters WHERE user_id == ?', (message.from_user.id, )).fetchone()
    
    