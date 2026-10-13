from login import login
from application_creation import apply_for_job
from submission_creation import submit_work


def user_panel(users, projects, jobs, applications, submissions):

    print("\n========================")
    print("       USER LOGIN")
    print("========================")

    current_user = login(users)

    if current_user is None:
        return

    while True:

        print("""
========================
       USER MENU
========================

1. View Profile
2. View Projects
3. View Jobs
4. Search Jobs
5. Apply for Job
6. My Applications
7. My Jobs
8. Start Job
9. Submit Work
10. Update Profile
11. Change Password
12. Logout
13. Back
""")

        choice = input("Enter choice: ")

        # VIEW PROFILE

        if choice == "1":

            print("\n===== MY PROFILE =====")

            print("ID:", current_user.id)
            print("Name:", current_user.name)
            print("Email:", current_user.email)
            print("Role:", current_user.role)
            print("Status:", current_user.status)

        # VIEW PROJECTS

        elif choice == "2":

            if len(projects) == 0:

                print("No projects available.")

                continue

            print("\n===== PROJECTS =====")

            for project in projects:

                print("Project ID:", project.id)
                print("Name:", project.name)
                print("Description:", project.description)
                print("Budget:", project.budget)
                print("Status:", project.status)

                print("--------------------")

        # VIEW JOBS

        elif choice == "3":

            if len(jobs) == 0:

                print("No jobs available.")

                continue

            print("\n===== AVAILABLE JOBS =====")

            found = False

            for job in jobs:

                if job.status == "Open":

                    found = True

                    print("Job ID:", job.id)
                    print("Project ID:", job.project_id)
                    print("Title:", job.title)
                    print("Description:", job.description)
                    print("Budget:", job.budget)
                    print("Priority:", job.priority)

                    print("--------------------")

            if not found:

                print("No open jobs available.")

        # SEARCH JOB

        elif choice == "4":

            job_id = int(input("Enter job ID: "))

            found = False

            for job in jobs:

                if job.id == job_id:

                    found = True

                    print("\n===== JOB FOUND =====")

                    print("Job ID:", job.id)
                    print("Project ID:", job.project_id)
                    print("Title:", job.title)
                    print("Description:", job.description)
                    print("Budget:", job.budget)
                    print("Priority:", job.priority)
                    print("Status:", job.status)

                    break

            if not found:

                print("Job not found.")

        # APPLY

        elif choice == "5":

            apply_for_job(
                applications,
                jobs,
                current_user
            )

        # MY APPLICATIONS

        elif choice == "6":

            print("\n===== MY APPLICATIONS =====")

            found = False

            for application in applications:

                if application.user_id == current_user.id:

                    found = True

                    print("Application ID:", application.id)
                    print("Job ID:", application.job_id)
                    print("Message:", application.message)
                    print("Status:", application.status)

                    print("--------------------")

            if not found:

                print("You have no applications.")

        # MY JOBS

        elif choice == "7":

            print("\n===== MY JOBS =====")

            found = False

            for job in jobs:

                if job.assigned_to == current_user.id:

                    found = True

                    print("Job ID:", job.id)
                    print("Title:", job.title)
                    print("Description:", job.description)
                    print("Budget:", job.budget)
                    print("Priority:", job.priority)
                    print("Status:", job.status)

                    print("--------------------")

            if not found:

                print("No jobs assigned to you.")

        # START JOB

        elif choice == "8":

            job_id = int(input("Enter job ID: "))

            found = False

            for job in jobs:

                if job.id == job_id:

                    found = True

                    if job.assigned_to != current_user.id:

                        print("This job is not assigned to you.")

                        break

                    if job.status == "Assigned":

                        job.status = "In Progress"

                        with open("jobs.txt", "w") as f:

                            for j in jobs:

                                f.write(
                                    f"{j.id}|"
                                    f"{j.project_id}|"
                                    f"{j.title}|"
                                    f"{j.description}|"
                                    f"{j.budget}|"
                                    f"{j.priority}|"
                                    f"{j.status}|"
                                    f"{j.assigned_to}\n"
                                )

                        print("Job started successfully.")

                    elif job.status == "Changes Required":

                        job.status = "In Progress"

                        with open("jobs.txt", "w") as f:

                            for j in jobs:

                                f.write(
                                    f"{j.id}|"
                                    f"{j.project_id}|"
                                    f"{j.title}|"
                                    f"{j.description}|"
                                    f"{j.budget}|"
                                    f"{j.priority}|"
                                    f"{j.status}|"
                                    f"{j.assigned_to}\n"
                                )

                        print("Job started again.")

                    else:

                        print("Job cannot be started from its current status.")

                    break

            if not found:

                print("Job not found.")

        # SUBMIT WORK

        elif choice == "9":

            submit_work(
                submissions,
                jobs,
                current_user
            )

        # UPDATE PROFILE

        elif choice == "10":

            print("\n===== UPDATE PROFILE =====")

            new_name = input("Enter new name: ")
            new_email = input("Enter new email: ")

            email_exists = False

            for user in users:

                if (
                    user.email == new_email
                    and user.id != current_user.id
                ):

                    email_exists = True

                    break

            if email_exists:

                print("Email already exists.")

            else:

                current_user.name = new_name
                current_user.email = new_email

                with open("users.txt", "w") as f:

                    for user in users:

                        f.write(
                            f"{user.id}|"
                            f"{user.name}|"
                            f"{user.email}|"
                            f"{user.password}|"
                            f"{user.role}|"
                            f"{user.status}\n"
                        )

                print("Profile updated successfully.")

        # CHANGE PASSWORD

        elif choice == "11":

            old_password = input("Enter old password: ")

            if old_password != current_user.password:

                print("Incorrect old password.")

            else:

                new_password = input("Enter new password: ")

                current_user.password = new_password

                with open("users.txt", "w") as f:

                    for user in users:

                        f.write(
                            f"{user.id}|"
                            f"{user.name}|"
                            f"{user.email}|"
                            f"{user.password}|"
                            f"{user.role}|"
                            f"{user.status}\n"
                        )

                print("Password changed successfully.")

        # LOGOUT

        elif choice == "12":

            print("Logged out.")

            return

        # BACK

        elif choice == "13":

            return

        else:

            print("Invalid choice.")