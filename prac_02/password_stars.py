"""
CP1404 - Practical 2
Simple password checker program.
"""

MINIMUM_LENGTH = 2


def main():
    """Get password and show as asterisks."""
    password = get_password()
    print_password(password)


def print_password(password):
    """Print password as asterisks."""
    print("*" * len(password))


def get_password():
    """Get valid password."""
    password = input("Password: ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Password must be {MINIMUM_LENGTH} long")
        password = input("Password: ")
    return password


main()
