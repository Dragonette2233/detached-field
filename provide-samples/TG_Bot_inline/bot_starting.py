import initDecorator # just for fun
from aiogram.utils import executor
from bot_creating import dp

@initDecorator.startGEN
def main():
    from handlers import client, admin, other
    client.register_handlers_client(dp)
    admin.register_handlers_admin(dp)
    other.register_handlers_other(dp)
    
    executor_dict = {
        'skip_updates': True,
        'on_startup': initDecorator.on_startup,
        'on_shutdown': initDecorator.on_shutdown
    }

    executor.start_polling(dp, **executor_dict)
    
    
if __name__ == '__main__':
    main()