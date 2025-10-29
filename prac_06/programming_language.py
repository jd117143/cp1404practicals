"""
CP1404 - Practical 6
ProgrammingLanguage class module.
Estimate: 20 minutes
Actual:
"""


class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object with key characteristics"""
    def __init__(self, typing="", reflection=False, year=0):
        """Initialise a ProgrammingLanguage instance.

        name: string, name of the language
        typing: string, typing style (e.g., Static/Dynamic)
        reflection: boolean, whether the language supports reflection
        year: integer, year the language first appeared
        """
        self.typing = typing
        self.reflection = reflection
        self.year = year
