"""
CP1404 - Practical 5
Hexadecimal colour dictionary
"""

NAME_TO_CODE = {"absolute zero": "#0048ba", "aliceblue": "#f0f8ff", "amaranth": "#e52b50", "beige": "#f5f5dc",
                "bistre": "#3d2b1f", "blond": "#faf0be", "cardinal": "#c41e3a", "carmine": "#960018",
                "citron": "#9fa91f", "eggshell": "#f0ead6", "frostbite": "#e936a7"}

colour_name = input("Colour name: ").lower()
while colour_name != "":
    try:
        print(colour_name.title(), "is", NAME_TO_CODE[colour_name])
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Colour name: ").lower()
