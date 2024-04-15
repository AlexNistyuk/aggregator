from datetime import datetime
from typing import Iterable

from pymongo.results import InsertManyResult

from src.managers.mongo_manager import DataBaseManager
from src.repositories.interfaces import IRepository
from src.utils.config import get_settings


class PaymentRepository(DataBaseManager, IRepository):
    collection = get_settings().payment_collection

    async def insert_many(self, documents: Iterable[dict]) -> InsertManyResult:
        return await self.db[self.collection].insert_many(documents)

    async def get_between_dates(self, date_from: datetime, date_to: datetime):
        return (
            await self.db[self.collection]
            .find({"dt": {"$gte": date_from, "$lte": date_to}})
            .to_list(length=None)
        )
