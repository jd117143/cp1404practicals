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

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a Project object."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation of a Project object."""
        start_date_string = self.start_date.strftime("%d/%m/%Y")
        return (f"{self.name}, start: {start_date_string}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Return True if the self priority is less than the other priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Return True if the project is completed."""
        return self.completion_percentage == 100

    def update_details(self, new_priority, new_completion_percentage):
        """Update priority or completion percentage if new non-blank values are given."""
        if new_priority != "":
            self.priority = int(new_priority)
        if new_completion_percentage != "":
            self.completion_percentage = int(new_completion_percentage)
