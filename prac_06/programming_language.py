"""
CP1404 - Practical 6
ProgrammingLanguage class module.
Estimate: 20 minutes
Actual: 24 minutes
(Time details for class module + client code combined)
"""


class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object with key characteristics"""

    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initialise a ProgrammingLanguage instance.

        name: string, name of the language
        typing: string, typing style (e.g., Static/Dynamic)
        reflection: boolean, whether the language supports reflection
        year: integer, year the language first appeared
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string representation of a ProgrammingLanguage object."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Return True if the language uses dynamic typing."""
        return self.typing.lower() == "dynamic"
