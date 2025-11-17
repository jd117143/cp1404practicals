"""
CP1404 - Practical 9
SilverServiceTaxi class (is a Taxi --> is a Car).
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness
