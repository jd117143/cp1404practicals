MINIMUM_LENGTH = 2


def main():
    password = get_password()
    print_password(password)


def print_password(password):
    print("*" * len(password))


def get_password():
    password = input("Password: ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Password must be {MINIMUM_LENGTH} long")
        password = input("Password: ")
    return password


main()
