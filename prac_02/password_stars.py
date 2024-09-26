MINIMUM_PASSWORD_LENGTH = 8

def main():
    password = get_password()
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print(f"Password must be at least {MINIMUM_PASSWORD_LENGTH} characters long.")
        password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))

def get_password():
    password = input('Enter a password: ')
    return password

main()