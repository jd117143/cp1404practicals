"""
CP1404 - Practical 9
SilverServiceTaxi class test code.
"""

from prac_09.silver_service_taxi import SilverServiceTaxi

fancy_taxi = SilverServiceTaxi("Fancy Taxi", 100, 2)
fancy_taxi.drive(18)

expected_fare = 48.78
actual_fare = fancy_taxi.get_fare()

assert expected_fare == actual_fare, f"Expected ${expected_fare}, but got ${actual_fare}"
print("Test successful. Correct fare calculation.")
