from aiogram import Router

from src.routers.v1.aggregation import router as aggregation_router

router = Router()

router.include_router(aggregation_router)
