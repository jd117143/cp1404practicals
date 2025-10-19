"""
CP1404 - Practical 5
Read, process, and display Wimbledon champions data
Estimate: 50 minutes
Actual:
"""

FILENAME = "wimbledon.csv"


def main():
    data = load_data(FILENAME)
    print(data)


def load_data(filename=FILENAME):
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            data.append(line.strip().split(','))
    return data


main()
