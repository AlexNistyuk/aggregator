from datetime import datetime


class DateRounder:
    @classmethod
    def round_by_month(cls, date: datetime) -> datetime:
        return datetime(date.year, date.month, day=1)

    @classmethod
    def round_by_day(cls, date: datetime) -> datetime:
        return datetime(date.year, date.month, date.day)

    @classmethod
    def round_by_hour(cls, date: datetime) -> datetime:
        return datetime(date.year, date.month, date.day, date.hour)
