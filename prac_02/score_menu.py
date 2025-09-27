"""
CP1404 - Practical 2
Menu-driven score program.
"""

from score import determine_status

MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    """Run the score menu program."""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            determine_status(score)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid input.")
        print(MENU)
        choice = input(">>> ").upper()
    print("Finished.")


def print_stars(score):
    """Print stars equal to score."""
    print("*" * score)


def get_valid_score():
    """Get a valid score (0-100)."""
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Score must be 0-100")
        score = int(input("Score: "))
    return score


main()
