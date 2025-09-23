"""
CP1404/CP5632 - Practical
Program to determine score status
"""
from random import randint


def main():
    score = randint(0, 100)
    # score = float(input("Enter score: "))    # For manual input
    print(score)
    determine_status(score)


def determine_status(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


main()
