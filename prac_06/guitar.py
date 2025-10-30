"""
CP1404 - Practical 6
Guitar class module.
Estimate: 15 minutes
Actual: 12 minutes
"""


class Guitar:
    """Represent a Guitar object with key characteristics."""
    CURRENT_YEAR = 2025
    VINTAGE_AGE = 50

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance.

        name: string, name of the guitar
        year: integer, year the guitar was first made
        cost: float, cost of the guitar
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar object."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of a guitar based on CURRENT_YEAR."""
        return Guitar.CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the guitar is more than or equal to VINTAGE_AGE."""
        return self.get_age() >= Guitar.VINTAGE_AGE
