import datetime

from dateutil.relativedelta import relativedelta

from src.repositories.payments import PaymentRepository
from src.services.interfaces import IService
from src.utils.config import get_settings
from src.utils.date import DateRounder

settings = get_settings()


class AggregationService(IService):
    round_map = {
        "hour": DateRounder.round_by_hour,
        "day": DateRounder.round_by_day,
        "month": DateRounder.round_by_month,
    }
    timedelta_map = {
        "hour": relativedelta(hours=1),
        "day": relativedelta(days=1),
        "month": relativedelta(months=1),
    }

    repository = PaymentRepository()

    async def get_aggregation_data(self, data: dict) -> dict:
        date_from = datetime.datetime.fromisoformat(data["dt_from"])
        date_to = datetime.datetime.fromisoformat(data["dt_upto"])
        date_rounder = self.round_map.get(data["group_type"])
        timedelta = self.timedelta_map.get(data["group_type"])

        payment_between_dates: list[dict] = await self.repository.get_between_dates(
            date_from, date_to
        )
        aggregated_data: dict = self.__get_aggregated_data(
            payment_between_dates, date_rounder
        )

        dataset = []
        labels = []

        while date_from <= date_to:
            if date_from in aggregated_data:
                dataset.append(aggregated_data[date_from])
            else:
                dataset.append(0)

            labels.append(date_from.isoformat())

            date_from += timedelta

        return {
            "dataset": dataset,
            "labels": labels,
        }

    def __get_aggregated_data(
        self, payment_between_dates: list[dict], date_rounder
    ) -> dict:
        result = {}
        for item in payment_between_dates:
            rounded_date = date_rounder(item["dt"])

            if rounded_date not in result:
                result[rounded_date] = item["value"]
            else:
                result[rounded_date] += item["value"]

        return result
