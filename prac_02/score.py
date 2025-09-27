"""
CP1404- Practical 2
Program to determine score status.
"""

from random import randint


def main():
    """Generate/get score, then show its status."""
    score = randint(0, 100)              # Generate random score
    # score = float(input("Enter score: "))    # Get manual input
    print(score)
    determine_status(score)


def determine_status(score):
    """Print the status for a score."""
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


main()
