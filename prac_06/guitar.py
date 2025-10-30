"""
CP1404 - Practical 6
Guitar class module.
Estimate: 15 minutes
Actual:
"""


class Guitar:
    """Represent a Guitar object with key characteristics."""

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
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Get the age of a guitar based on the current year."""
        return 2025 - self.year

    def is_vintage(self):
        """Determine if a guitar is vintage based on its age."""
        return self.get_age() >= 50
