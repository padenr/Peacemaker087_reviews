import datetime


class DateValidator:

    @classmethod
    def is_valid_date(cls, day: int = 1, month: int = 1, year: int = 1) -> None:
        try:
            datetime.date(year, month, day)
        except ValueError:
            raise ValueError(f"Invalid date")


class Date:

    def __init__(self, day: int, month: int, year: int):
        self._day = day
        self._month = month
        self._year = year
        DateValidator.is_valid_date(self._day, self._month, self._year)

    def __str__(self):
        return f"{self._day}/{self._month}/{self._year}"


class MonthYearDate(Date):

    def __init__(self, month: int, year: int):
        self._month = month
        self._year = year
        DateValidator.is_valid_date(month=self._month, year=self._year)

    def __str__(self):
        return f"{self._month}/{self._year}"
    

class YearDate(Date):

    def __init__(self, year: int):
        self._year = year
        DateValidator.is_valid_date(year=self._year)

    def __str__(self):
        return f"{self._year}"