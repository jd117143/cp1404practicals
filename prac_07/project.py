"""
CP1404 - Practical 7
Project class module.
Estimate: 1 hour, 30 minutes
Actual:
(Time details for Project class module + project management combined)
"""


class Project:
    """Represent a Project object with key characteristics."""

    def __init__(self, name, start_date, cost_estimate, completion_percentage):
        """Initialise a Project object."""
        self.name = name
        self.start_date = start_date
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage
