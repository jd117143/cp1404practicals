"""
CP1404 - Practical 3
Demonstrates exception handling with ValueError and ZeroDivisionError.
Includes answers to:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

# 1. A ValueError will occur when the input isn't an integer.
# Broadly speaking, it will occur when a function (e.g. int()) receives the correct
# type but invalid value.
# 2. A ZeroDivisionError will occur when the input for the denominator is a 0.
# 3. Yes, via a while loop check for example, as shown above.
