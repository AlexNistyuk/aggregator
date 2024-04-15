from aiogram import Dispatcher

from src.routers.routers import router as api_router


def init_routers(dp: Dispatcher):
    dp.include_router(api_router)
