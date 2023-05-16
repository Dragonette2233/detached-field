from database import sqlite_db

def startGEN(func):
    def innitializing(*args, **kwargs):
        print(f'Initializing [definition -- [FUFO Monkey Journey]')
        result = func()
    
    return innitializing

async def on_startup(_):
    '''Startup message'''
    print('Bot ready: 100%')
    sqlite_db.sql_start()

async def on_shutdown(_):
    '''Closing message'''
    print('Bot shutdowned: 100%')