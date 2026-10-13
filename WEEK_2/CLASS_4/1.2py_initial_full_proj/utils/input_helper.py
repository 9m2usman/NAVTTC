def get_string(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty.")


def get_integer(prompt, minimum=None):
    while True:
        try:
            value = int(input(prompt))

            if minimum is not None and value < minimum:
                print(f"Value must be at least {minimum}.")
                continue

            return value

        except ValueError:
            print("Please enter a valid integer.")


def get_float(prompt, minimum=None):
    while True:
        try:
            value = float(input(prompt))

            if minimum is not None and value < minimum:
                print(f"Value must be at least {minimum}.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")


def get_choice(prompt, valid_choices):
    while True:
        choice = input(prompt).strip()

        if choice in valid_choices:
            return choice

        print("Invalid choice.")


def confirm(prompt="Are you sure? (y/n): "):
    while True:
        choice = input(prompt).strip().lower()

        if choice in ("y", "yes"):
            return True

        if choice in ("n", "no"):
            return False

        print("Please enter y or n.")