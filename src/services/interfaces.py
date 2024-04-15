from abc import ABC, abstractmethod

from src.repositories.interfaces import IRepository


class IService(ABC):
    repository: IRepository

    @abstractmethod
    async def get_aggregation_data(self, *args, **kwargs):
        raise NotImplementedError
