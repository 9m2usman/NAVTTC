from registration import register
from admin_panel import admin_panel
from user_panel import user_panel
from user import User
from load_users import load_users
from load_projects import load_projects
from load_jobs import load_jobs
from load_applications import load_applications
from load_submissions import load_submissions


users = load_users()
projects = load_projects()
jobs = load_jobs()
applications = load_applications()
submissions = load_submissions()

if len(users) == 0:

    admin = User(1,"Admin","admin@gmail.com","admin123","Admin","Active")

    users.append(admin)

    with open("users.txt", "a") as f:

        f.write(
            f"{admin.id}|"
            f"{admin.name}|"
            f"{admin.email}|"
            f"{admin.password}|"
            f"{admin.role}|"
            f"{admin.status}\n"
        )

def main():

    while True:

        print("""
========================
 PROJECT MANAGEMENT SYSTEM

1. Admin
2. User
3. Registration
4. Exit
""")

        choice = input("Enter choice: ")

        if choice == "1":

            admin_panel(users,projects,jobs,applications,submissions)

        elif choice == "2":

            user_panel(users,projects,jobs,applications,submissions)

        elif choice == "3":

            register(users)

        elif choice == "4":

            print("Goodbye.")

            break

        else:

            print("Invalid choice.")


if __name__ == "__main__":

    main()