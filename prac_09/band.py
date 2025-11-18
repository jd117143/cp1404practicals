"""
CP1404 - Practical 9
Band class.
"""


class Band:
    """Represent a Band object."""

    def __init__(self, name=""):
        """Initialise a Band."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({self.musicians})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing their first (or no) instrument."""
        return "\n".join(musician.play() for musician in self.musicians)
