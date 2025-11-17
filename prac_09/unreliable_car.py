"""
CP1404 - Practical 9
UnreliableCar class (is a Car).
"""

from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on Car"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car, but only if it's reliable enough"""
        if randint(1, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0
