import json

from aiogram import Router
from aiogram.types import Message

from src.services.aggregation import AggregationService

router = Router()


@router.message()
async def get_aggregation_data(message: Message):
    json_data = json.loads(message.text)

    aggregation_data = await AggregationService().get_aggregation_data(json_data)

    await message.answer(json.dumps(aggregation_data))
