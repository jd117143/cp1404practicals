"""
CP1404 - Practical 9
Taxi simulator program.
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Run taxi simular program via menu."""
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            pass
        elif choice == "D":
            pass
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()


def choose_taxi():
    pass


def drive_taxi():
    pass


if __name__ == '__main__':
    main()
