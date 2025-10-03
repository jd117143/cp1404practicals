"""
CP1404 - Practical 3
Program repeatedly prompts until user enters a valid integer.
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True
    except ValueError:
        print("Please enter an integer.")
print("Valid result is:", result)
