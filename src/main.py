import asyncio
import logging

from aiogram import Bot, Dispatcher

from src.utils.config import get_settings

logging.basicConfig(level=logging.INFO)

bot = Bot(token=get_settings().bot_token.get_secret_value())
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
