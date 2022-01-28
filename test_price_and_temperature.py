from unittest import TestCase
from price_and_temperature import unit_price, celsius_to_fahrenheit


class Test(TestCase):
    def test_unit_price(self):
        self.assertEqual(unit_price(), f"This product is ¥{60/30}/kg")

    def test_celsius_to_fahrenheit(self):
        self.assertEqual(celsius_to_fahrenheit(), f"{50}°C is {122.0}°F")
