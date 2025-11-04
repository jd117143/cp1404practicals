"""
CP1404 - Practical 6
Guitar class basic test code.
Estimate: 10 minutes
Actual: 10 minutes
"""

from prac_06.guitar import Guitar


def main():
    """Test Guitar class."""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    line = Guitar("Line 6 JTV-59", 2010, 1512.9)
    print(f"{gibson.name} get_age() - Expected {103}. Got {gibson.get_age()}")
    print(f"{line.name} get_age() - Expected {15}. Got {line.get_age()}")
    print(f"{gibson.name} is_vintage() - Expected {True}. Got {gibson.is_vintage()}")
    print(f"{line.name} is_vintage() - Expected {False}. Got {line.is_vintage()}")


if __name__ == "__main__":
    main()
