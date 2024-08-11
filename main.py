import asyncio
import contextlib
import logging
from datetime import datetime
from aiogram import Bot, Dispatcher
from aiogram.filters import Text, Command
from aiogram.types import BotCommand

from Defs.Bot import bot
from Defs.Config import BOTUSERNAME, ADMIN_ID, LOGNAME
from Defs.Defs import on_start
from Defs.Defs_Admin import on_start_admin, run_db_export, run_ping_bot, run_logs_export
from Defs.Defs_Demo import run_demo, end_of_demo, tarifs
from Defs.State_Machine import States


# Регистрация команд, отображаемых в интерфейсе Telegram
async def set_commands(bot: Bot):
    commands = [BotCommand(command="/start", description="Старт"),]
    await bot.set_my_commands(commands)


async def start_bot(bot: Bot):
    await bot.send_message(chat_id=ADMIN_ID, text='Бот запущен')
    date_time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f'{BOTUSERNAME} запущен {date_time_now}')


async def stop_bot(bot: Bot):
    await bot.send_message(chat_id=ADMIN_ID, text='Бот остановлен')
    date_time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f'{BOTUSERNAME} остановлен {date_time_now}')


async def start():
    logging.basicConfig(level=logging.WARNING,  # WARNING  INFO
                        filename=LOGNAME,
                        format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
                        datefmt='%H:%M:%S',
                        )
    # bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(on_start, Command(commands=['start']))
    dp.message.register(on_start, Text(text='Начать заново'))
    dp.message.register(tarifs, Text(text='Тарифы'))
    dp.message.register(run_demo, States.demo)
    dp.message.register(end_of_demo, States.end)

    # Админ
    dp.message.register(on_start_admin, Command(commands=['start']))
    dp.message.register(on_start_admin, Text(text='Начать заново'))
    dp.message.register(run_db_export, Text(text='База Полная'))
    # dp.message.register(run_db_export_short, Text(text='База Краткая'))
    dp.message.register(run_ping_bot, Text(text='PING'))
    dp.message.register(run_logs_export, Text(text='ЛОГИ'))

    await set_commands(bot)  # Установка команд бота

    try:
        logging.error(f'OK - - - - - - - - - - - - - - - - - - - - OK\n\n'
                      f'[{BOTUSERNAME} started successful]: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', exc_info=True)
        await dp.start_polling(bot)
    except Exception as ex:
        logging.error(f"[!!! Exception] - {ex}", exc_info=True)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(start())
