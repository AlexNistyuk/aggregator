from aiogram import Router

from src.routers.v1.routers import router as v1_router

router = Router()

router.include_router(v1_router)
