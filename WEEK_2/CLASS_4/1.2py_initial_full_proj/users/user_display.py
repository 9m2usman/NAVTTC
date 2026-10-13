def display_user(user):
    print(
        f"ID: {user['id']}\n"
        f"Username: {user['username']}\n"
        f"Role: {user['role']}\n"
        f"Status: {user['status']}"
    )


def display_users(users):

    if not users:
        print("No users found.")
        return

    print("-" * 60)
    print(
        f"{'ID':<8}"
        f"{'USERNAME':<20}"
        f"{'ROLE':<15}"
        f"{'STATUS':<10}"
    )
    print("-" * 60)

    for user in users:
        print(
            f"{user['id']:<8}"
            f"{user['username']:<20}"
            f"{user['role']:<15}"
            f"{user['status']:<10}"
        )

    print("-" * 60)