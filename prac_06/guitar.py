"""
CP1404 - Practical 6
Guitar class module.
Estimate: 15 minutes
Actual:
"""


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"
