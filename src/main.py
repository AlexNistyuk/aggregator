import asyncio
import logging

from aiogram import Bot, Dispatcher

from src.managers.mongo_manager import DataBaseManager
from src.routers.init import init_routers
from src.utils.config import get_settings

logging.basicConfig(level=logging.INFO)


bot = Bot(token=get_settings().bot_token.get_secret_value())
dp = Dispatcher()

init_routers(dp)


async def main():
    await DataBaseManager.connect()

    await dp.start_polling(bot)

    await DataBaseManager.close()


if __name__ == "__main__":
    asyncio.run(main())
