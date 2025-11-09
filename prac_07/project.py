"""
CP1404 - Practical 7
Project class module.
Estimate: 1 hour, 30 minutes
Actual:
(Time details for Project class module + project management combined)
"""

import datetime


class Project:
    """Represent a Project object with key characteristics."""

    def __init__(self, name, start_date, cost_estimate, completion_percentage):
        """Initialise a Project object."""
        self.name = name
        self.start_date = start_date
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation of a Guitar object."""
        start_date_string = self.start_date.strftime("%d/%m/%Y")
        return (f"{self.name}, start: {start_date_string},"
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")
