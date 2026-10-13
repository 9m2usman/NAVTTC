from user import User


def register(users):

    print("\n=====REGISTRATION=====")

    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    for user in users:

        if user.email == email:

            print("Email already exists.")
            return

    user_id = len(users) + 1

    new_user = User(user_id,name,email,password)

    users.append(new_user)

    with open("users.txt", "a") as file:

        file.write(
            f"{new_user.id}|"
            f"{new_user.name}|"
            f"{new_user.email}|"
            f"{new_user.password}|"
            f"{new_user.role}|"
            f"{new_user.status}\n"
        )

    print("Registration successful.")