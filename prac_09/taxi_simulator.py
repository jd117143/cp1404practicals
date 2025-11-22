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
    bill_to_date = 0.0

    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            current_taxi = choose_taxi(taxis)
        elif choice == "D":
            trip_cost = drive_taxi(current_taxi)
            bill_to_date += trip_cost
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        choice = input(">>> ").upper()


def choose_taxi(taxis):
    """Get taxi based on user input."""
    print("Taxis available:")
    display_taxis(taxis)
    try:
        taxi_choice = int(input("Choose taxi: "))
        return taxis[taxi_choice]
    except (ValueError, IndexError):
        print("Invalid taxi choice")


def drive_taxi(current_taxi):
    """Drive chosen taxi."""
    if current_taxi:
        current_taxi.start_fare()
        distance = float(input("Drive how far? "))
        current_taxi.drive(distance)
        trip_cost = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
        return trip_cost
    else:
        print("You need to choose a taxi before you can drive")
        return 0


def display_taxis(taxis):
    """Display all taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == '__main__':
    main()
