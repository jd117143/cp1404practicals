"""
CP1404 - Practical 5
Read, process, and display Wimbledon champions data
Estimate: 50 minutes
Actual:
"""

FILENAME = "wimbledon.csv"


def main():
    data = load_data(FILENAME)
    countries, champion_to_count = process_data(data)
    display_results(countries, champion_to_count)


def load_data(filename=FILENAME):
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            data.append(line.strip().split(','))
    return data


def process_data(data):
    countries = {entry[1] for entry in data}

    champion_to_count = {}
    for entry in data:
        champion = entry[2]
        count = champion_to_count.get(champion, 0)
        champion_to_count[champion] = count + 1
    return countries, champion_to_count


def display_results(countries, champion_to_count):
    print("Wimbledon Champions: ")
    for champion, count in champion_to_count.items():
        print(f"{champion} {count}")
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))


main()
