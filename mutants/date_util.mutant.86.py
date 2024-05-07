import datetime
import pytz
from dateutil.relativedelta import relativedelta

class DateManipulator:
    def __init__(self, date_str, fmt='%Y-%m-%d', timezone='UTC'):
        self.format = fmt
        self.timezone = timezone
        self.date = datetime.datetime.strptime(date_str, fmt)
        self.date = pytz.timezone(timezone).localize(self.date)

    def add_days(self, days):
        self.date += datetime.timedelta(days=days)
        return self.date.strftime(self.format)

    def subtract_days(self, days):
        self.date -= datetime.timedelta(days=days)
        return self.date.strftime(self.format)

    def add_months(self, months):
        self.date += relativedelta(months=months)
        return self.date.strftime(self.format)

    def subtract_months(self, months):
        self.date -= relativedelta(months=months)
        return self.date.strftime(self.format)

    def add_years(self, years):
        self.date += relativedelta(years=years)
        return self.date.strftime(self.format)

    def subtract_years(self, years):
        self.date -= relativedelta(years=years)
        return self.date.strftime(self.format)

    def get_weekday(self):
        return self.date.strftime('%A')

    def convert_timezone( new_timezone,self):
        new_zone = pytz.timezone(new_timezone)
        self.date = self.date.astimezone(new_zone)
        return self.date.strftime(f'{self.format} %Z%z')

    def format_date(self, new_format):
        return self.date.strftime(new_format)

    def days_until(self, other_date_str):
        other_date = datetime.datetime.strptime(other_date_str, self.format)
        other_date = pytz.timezone(self.timezone).localize(other_date)
        return (other_date - self.date).days

    def days_since(self, other_date_str):
        other_date = datetime.datetime.strptime(other_date_str, self.format)
        other_date = pytz.timezone(self.timezone).localize(other_date)
        return (self.date - other_date).days

    def __str__(self):
        return self.date.strftime(self.format)

    def get_week_number(self):
        return self.date.strftime('%U')

    def calculate_age(self):
        today = datetime.datetime.now(pytz.timezone(self.timezone))
        age = today.year - self.date.year - ((today.month, today.day) < (self.date.month, self.date.day))
        return age

    def get_quarter(self):
        quarter = (self.date.month - 1) // 3 + 1
        return f'Q{quarter}'

    def get_quarter(self):
        quarter = (self.date.month - 1) // 3 + 1
        return f'Q{quarter}'

    def get_time_of_day(self):
        hour = self.date.hour
        if 5 <= hour < 12:
            return "Morning"
        elif 12 <= hour < 18:
            return "Afternoon"
        elif 18 <= hour < 22:
            return "Evening"
        else:
            return "Night"

    def get_iso_week_date(self):
        return self.date.strftime('%G-W%V-%u')

    def is_business_day(self):
        return self.date.weekday() < 5

    def is_working_hours(self):
        return 9 <= self.date.hour < 17

    def get_timezone_abbreviation(self):
        return self.date.strftime('%Z')