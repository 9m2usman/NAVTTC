from registration import register

def login(users):

    print("\n=====LOGIN=====")

    email = input("Enter your email: ")
    password = input("Enter your password: ")

    for user in users:

        if user.email == email:

            if user.password == password:

                if user.status == "Active":

                    print("Login successful.")

                    return user

                else:

                    print("Account is inactive.")

                    return None

            else:

                print("Invalid password.")

                return None

    print("Email not found.")

    choice = input("Do you want to register? (y/n): ")

    if choice.lower() == "y":

        register(users)

    return None