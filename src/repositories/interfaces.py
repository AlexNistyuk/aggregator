from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    async def insert_many(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def get_between_dates(self, *args, **kwargs):
        raise NotImplementedError
