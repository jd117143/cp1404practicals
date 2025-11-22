"""
CP1404 - Practical 9
UnreliableCar class client code.
"""

from prac_09.unreliable_car import UnreliableCar

low_reliability_car = UnreliableCar("Low Reliability Car", 100, 10)
high_reliability_car = UnreliableCar("High Reliability Car", 100, 90)

low_reliability_drive_count = 0
high_reliability_drive_count = 0

for attempt in range(100):
    if low_reliability_car.drive(1):
        low_reliability_drive_count += 1
    if high_reliability_car.drive(1):
        high_reliability_drive_count += 1

print(f"{low_reliability_car.name} drove {low_reliability_drive_count}x"f"...Expected ~{low_reliability_car.reliability}%")
print(f"{high_reliability_car.name} drove {high_reliability_drive_count}x"
      f"...Expected ~{high_reliability_car.reliability}%")
