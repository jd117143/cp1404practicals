"""
CP1404 - Practical 5
Read, process, and display Wimbledon champions data
Estimate: 50 minutes
Actual:
"""

FILENAME = "wimbledon.csv"


def main():
    """Run the Wimbledon data program."""
    entries = load_data(FILENAME)
    countries, champion_to_count = process_data(entries)
    display_results(countries, champion_to_count)


def load_data(filename=FILENAME):
    """Load data from CSV file and return a list of entries."""
    entries = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            entries.append(line.strip().split(','))
    return entries


def process_data(entries):
    """Extract countries and count how many times each champion has won."""
    countries = {entry[1] for entry in entries}

    champion_to_count = {}
    for entry in entries:
        champion = entry[2]
        count = champion_to_count.get(champion, 0)
        champion_to_count[champion] = count + 1
    return countries, champion_to_count


def display_results(countries, champion_to_count):
    """Display champions with their win counts and the list of countries."""
    print("Wimbledon Champions: ")
    for champion, count in champion_to_count.items():
        print(f"{champion} {count}")
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))


main()
