import unittest
from date_util import *

class TestDateManipulator(unittest.TestCase):
    def setUp(self):
        # Initializing with a fixed date for consistency in tests
        self.dm = DateManipulator('2023-01-15', timezone='UTC')

    def test_add_days(self):
        self.assertEqual(self.dm.add_days(10), '2023-01-25')

    def test_subtract_days(self):
        self.assertEqual(self.dm.subtract_days(15), '2022-12-31')

    def test_add_months(self):
        self.assertEqual(self.dm.add_months(2), '2023-03-15')

    def test_subtract_months(self):
        self.assertEqual(self.dm.subtract_months(1), '2022-12-15')

    def test_add_years(self):
        self.assertEqual(self.dm.add_years(1), '2024-01-15')

    def test_subtract_years(self):
        self.assertEqual(self.dm.subtract_years(1), '2022-01-15')

    def test_get_weekday(self):
        self.assertEqual(self.dm.get_weekday(), 'Sunday')

    def test_convert_timezone(self):
        self.assertIn('PST', self.dm.convert_timezone('US/Pacific'))

    def test_format_date(self):
        pass

    def test_days_until(self):
        self.assertEqual(self.dm.days_until('2023-02-15'), 31)

    def test_days_since(self):
        self.assertEqual(self.dm.days_since('2023-01-01'), 14)

    def test_get_week_number(self):
        self.assertEqual(self.dm.get_week_number(), '03')

    def test_calculate_age(self):
        # Assuming current year is 2023 and after January 15
        self.assertEqual(self.dm.calculate_age(), 1)

    def test_get_quarter(self):
        self.assertEqual(self.dm.get_quarter(), 'Q1')

    def test_get_time_of_day(self):
        # Assuming time is set to 00:00
        self.assertEqual(self.dm.get_time_of_day(), 'Night')

    def test_get_iso_week_date(self):
        self.assertEqual(self.dm.get_iso_week_date(), '2023-W02-7')

    def test_is_business_day(self):
        self.assertTrue(self.dm.is_business_day())

    def test_is_working_hours(self):
        # Assuming time is not set to working hours in initial setup
        self.assertFalse(self.dm.is_working_hours())

    def test_get_timezone_abbreviation(self):
        self.assertEqual(self.dm.get_timezone_abbreviation(), 'UTC')

# Run the test suite
if __name__ == '__main__':
    unittest.main()
