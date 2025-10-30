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
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ")

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        if guitar.is_vintage():
            vintage_string = " (vintage)"
        else:
            vintage_string = ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


if __name__ == "__main__":
    main()
