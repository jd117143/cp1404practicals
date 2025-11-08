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

    guitars.sort()

    for guitar in guitars:
        print(guitar)


def load_guitars(guitars):
    in_file = open('guitars.csv')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()


def add_new_guitar(guitars):
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ")


if __name__ == "__main__":
    main()
