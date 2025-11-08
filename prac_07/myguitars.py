"""
CP1404 - Practical 7
Guitar program.
"""

from prac_07.guitar import Guitar


def main():
    """Run Guitar program."""
    guitars = []

    load_guitars(guitars)
    add_new_guitar(guitars)
    save_guitars(guitars)

    guitars.sort()

    for guitar in guitars:
        print(guitar)


def load_guitars(guitars):
    """Load guitars from CSV file."""
    in_file = open("guitars.csv")
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()


def add_new_guitar(guitars):
    """Add new guitar entry."""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ")


def save_guitars(guitars):
    """Save guitars to CSV file."""
    with open("guitars.csv", "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


if __name__ == "__main__":
    main()
