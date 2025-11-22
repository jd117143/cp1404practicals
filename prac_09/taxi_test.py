"""
CP1404 - Practical 9
Taxi class client code.
"""

from prac_09.taxi import Taxi

my_taxi = Taxi("Prius 1", 100)
print(f"Initial:\n{my_taxi}")
print(f"Current fare: ${my_taxi.get_fare()}\n")
my_taxi.drive(40)
print(f"After 40km:\n{my_taxi}")
print(f"Current fare: ${my_taxi.get_fare()}\n")
my_taxi.start_fare()
my_taxi.drive(100)
print(f"Reset...then after 100km:\n{my_taxi}")
print(f"Current fare: ${my_taxi.get_fare()}\n")
