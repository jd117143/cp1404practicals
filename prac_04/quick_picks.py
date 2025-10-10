from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 45
LINE_NUMBER = 6


def main():
    number_of_quick_picks = int(input("How many quick picks? "))

    while number_of_quick_picks < 0:
        print("Try again")
        number_of_quick_picks = int(input("How many quick picks? "))

    for pick_number in range(number_of_quick_picks):
        quick_picks = []
        generate_numbers(quick_picks)
        print(" ".join(f"{number:2}" for number in sorted(quick_picks)))


def generate_numbers(quick_picks):
    while len(quick_picks) < LINE_NUMBER:
        number = randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_picks:
            quick_picks.append(number)


main()
