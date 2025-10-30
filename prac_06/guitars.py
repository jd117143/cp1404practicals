"""
CP1404 - Practical 6
Guitar program.
Estimate: 20 minutes
Actual:
"""

from prac_06.guitar import Guitar


def main():
    """Run Guitar program."""
    print("My guitars!")
    guitars = []

    name = input("Name: ")
    while name != "":
        year = input("Year: ")
        cost = input("Cost: $")
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ")


if __name__ == "__main__":
    main()
