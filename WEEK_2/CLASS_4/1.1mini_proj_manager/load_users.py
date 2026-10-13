from user import User

def load_users():

    users = []

    try:

        with open("users.txt", "r") as f:

            for line in f:

                line = line.strip()

                if line == "":
                    continue

                data = line.split("|")

                user_id = int(data[0])
                name = data[1]
                email = data[2]
                password = data[3]
                role = data[4]
                status = data[5]

                user = User(user_id, name, email, password, role, status)

                users.append(user)

    except FileNotFoundError:

        print("users.txt not found. Starting with empty users.")

    return users