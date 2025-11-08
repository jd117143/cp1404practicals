"""
CP1404 - Practical 7
Guitar program.
"""

from prac_07.guitar import Guitar


def main():
    """Run Guitar program."""
    guitars = []
    in_file = open('guitars.csv')
    in_file.readline()

    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()

    guitars.sort()

    for guitar in guitars:
        print(guitar)


if __name__ == "__main__":
    main()
