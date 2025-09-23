MINIMUM_LENGTH = 2


def main():
    password = input("Password: ")

    while len(password) < MINIMUM_LENGTH:
        print(f"Password must be {MINIMUM_LENGTH} long")
        password = input("Password: ")

    print("*" * len(password))


main()
