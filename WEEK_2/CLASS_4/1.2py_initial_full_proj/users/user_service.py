from storage.file_handler import read_file, write_file
from users.user_validation import (
    validate_username,
    validate_password,
    validate_role
)
from users.user_display import display_users


USER_FILE = "data/users.txt"

users = []


def load_users():

    global users

    users = []

    data = read_file(USER_FILE)

    for line in data:

        line = line.strip()

        if not line:
            continue

        parts = line.split("|")

        if len(parts) == 5:

            user = {
                "id": int(parts[0]),
                "username": parts[1],
                "password": parts[2],
                "role": parts[3],
                "status": parts[4]
            }

            users.append(user)


def save_users():

    data = []

    for user in users:

        line = (
            f"{user['id']}|"
            f"{user['username']}|"
            f"{user['password']}|"
            f"{user['role']}|"
            f"{user['status']}\n"
        )

        data.append(line)

    write_file(USER_FILE, data)


def add_user():

    print("\n========== ADD USER ==========")

    user_id = int(input("User ID: "))
    username = input("Username: ")
    password = input("Password: ")
    role = input("Role (Admin/Employee): ").lower()

    if not validate_username(username):
        print("Username cannot be empty.")
        return

    if not validate_password(password):
        print("Password must contain at least 6 characters.")
        return

    if not validate_role(role):
        print("Invalid role.")
        return

    for user in users:

        if user["id"] == user_id:
            print("User ID already exists.")
            return

        if user["username"].lower() == username.lower():
            print("Username already exists.")
            return

    user = {
        "id": user_id,
        "username": username,
        "password": password,
        "role": role,
        "status": "active"
    }

    users.append(user)

    save_users()

    print("User added successfully.")


def view_users():
    display_users(users)


def search_user():

    username = input("Enter username to search: ").lower()

    result = [
        user
        for user in users
        if username in user["username"].lower()
    ]

    display_users(result)


def login():

    print("\n========== LOGIN ==========")

    username = input("Username: ")
    password = input("Password: ")

    for user in users:

        if (
            user["username"].lower() == username.lower()
            and user["password"] == password
            and user["status"] == "active"
        ):

            print(f"Login successful. Welcome {user['username']}!")

            return user

    print("Invalid username or password.")

    return None


def update_user():

    user_id = int(input("Enter User ID: "))

    user = next(
        (u for u in users if u["id"] == user_id),
        None
    )

    if user is None:
        print("User not found.")
        return

    print("""
1. Username
2. Password
3. Role
4. Status
""")

    choice = input("Choice: ")

    if choice == "1":

        username = input("New username: ")

        if not validate_username(username):
            print("Invalid username.")
            return

        user["username"] = username

    elif choice == "2":

        password = input("New password: ")

        if not validate_password(password):
            print("Password must contain at least 6 characters.")
            return

        user["password"] = password

    elif choice == "3":

        role = input("New role: ").lower()

        if not validate_role(role):
            print("Invalid role.")
            return

        user["role"] = role

    elif choice == "4":

        status = input("Status (active/inactive): ").lower()

        if status not in ["active", "inactive"]:
            print("Invalid status.")
            return

        user["status"] = status

    else:
        print("Invalid choice.")
        return

    save_users()

    print("User updated successfully.")


def delete_user():

    user_id = int(input("User ID: "))

    for user in users:

        if user["id"] == user_id:

            users.remove(user)

            save_users()

            print("User deleted successfully.")

            return

    print("User not found.")


def user_menu():

    load_users()

    while True:

        print("""
========================================
             USER MANAGEMENT
========================================

1. Add User
2. View Users
3. Search User
4. Login
5. Update User
6. Delete User
7. Exit

========================================
""")

        choice = input("Enter choice: ")

        if choice == "1":
            add_user()

        elif choice == "2":
            view_users()

        elif choice == "3":
            search_user()

        elif choice == "4":
            login()

        elif choice == "5":
            update_user()

        elif choice == "6":
            delete_user()

        elif choice == "7":
            break

        else:
            print("Invalid choice.")