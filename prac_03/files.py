"""
CP1404 - Practical 3
File reading and writing examples.
"""

# 1. Write name to file
name = input("Name: ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

# 2. Read name from file and greet
in_file = open("name.txt")
name = in_file.read().strip()
print(f"Hi {name}!")
in_file.close()

# 3. Add first two numbers
with open("numbers.txt") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
    print(first_number + second_number)

# 4. Sum all numbers
total = 0
with open("numbers.txt") as in_file:
    for line in in_file:
        total += int(line)
print(total)
