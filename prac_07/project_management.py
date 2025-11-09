"""
CP1404 - Practical 7
Project Management program.
Estimate: 1 hour, 30 minutes
Actual:
(Time details for Project class module + project management combined)
"""

import datetime
from prac_07.project import Project

FILENAME = "projects.txt"
MENU = """
- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit
"""


def main():
    """Run the Project Management program."""
    print("Welcome to Project Manager")

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


if __name__ == '__main__':
    main()
