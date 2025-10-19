"""
CP1404 - Practical 5
Email to name dictionary
Estimate: 40 minutes
Actual:
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        username = email.split('@')[0]
        parts = username.split('.')
        name = ' '.join(parts).title()
        name_check = input(f"Is your name {name} (Y/n) ").upper()
        if name_check != 'Y':
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


main()
