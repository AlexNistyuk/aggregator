from datetime import datetime


class DateRounder:
    @classmethod
    def round_by_year(cls, date: datetime) -> datetime:
        return datetime(date.year, 1, 1)

    @classmethod
    def round_by_month(cls, date: datetime) -> datetime:
        return datetime(date.year, date.month, day=1)

    @classmethod
    def round_by_day(cls, date: datetime) -> datetime:
        return datetime(date.year, date.month, date.day)

    @classmethod
    def round_by_minute(cls, date: datetime) -> datetime:
        return datetime(date.year, date.month, date.day, date.minute)
