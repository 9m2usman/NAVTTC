from login import login
from project_creation import create_project
from job_creation import create_job

def admin_panel(users,projects,jobs,applications,submissions):

    print("\n========================")
    print("      ADMIN LOGIN")

    current_admin = login(users)

    if current_admin is None:
        return

    if current_admin.role != "Admin":

        print("Access denied. Admin access required.")

        return

    print("\n========================")
    print("     ADMIN DASHBOARD")

    while True:

        print("""
1. View Users
2. Search User
3. Activate/Deactivate User
4. Create Project
5. View Projects
6. Search Projects
7. Update Project Status
8. Delete Project
9. Create Job
10. View Jobs
11. Search Jobs
12. Update Job Status
13. View Applications
14. Approve Application
15. Reject Application
16. View Submissions
17. Review Submission
18. Reports
19. Logout
20. Back
""")

        choice = input("Enter choice: ")

        # VIEW USERS

        if choice == "1":

            print("\n===== ALL USERS =====")

            if len(users) == 0:

                print("No users.")

                continue

            for user in users:

                print("ID:", user.id)
                print("Name:", user.name)
                print("Email:", user.email)
                print("Role:", user.role)
                print("Status:", user.status)

                print("--------------------")

        # SEARCH USER

        elif choice == "2":

            email = input("Enter user email: ")

            found = False

            for user in users:

                if user.email == email:

                    print("\n===== USER FOUND =====")

                    print("ID:", user.id)
                    print("Name:", user.name)
                    print("Email:", user.email)
                    print("Role:", user.role)
                    print("Status:", user.status)

                    found = True

                    break

            if not found:

                print("User not found.")

        # ACTIVATE / DEACTIVATE USER

        elif choice == "3":

            user_id = int(input("Enter user ID: "))

            found = False

            for user in users:

                if user.id == user_id:

                    found = True

                    if user.id == current_admin.id:

                        print("You cannot deactivate yourself.")

                        break

                    print("Current Status:", user.status)

                    if user.status == "Active":

                        user.status = "Inactive"

                    else:

                        user.status = "Active"

                    with open("users.txt", "w") as f:

                        for u in users:

                            f.write(
                                f"{u.id}|"
                                f"{u.name}|"
                                f"{u.email}|"
                                f"{u.password}|"
                                f"{u.role}|"
                                f"{u.status}\n"
                            )

                    print("User status updated.")

                    break

            if not found:

                print("User not found.")

        # CREATE PROJECT

        elif choice == "4":

            create_project(projects)

        # VIEW PROJECTS

        elif choice == "5":

            print("\n===== ALL PROJECTS =====")

            if len(projects) == 0:

                print("No projects.")

                continue

            for project in projects:

                print("Project ID:", project.id)
                print("Project Name:", project.name)
                print("Project Description:", project.description)
                print("Project Budget:", project.budget)
                print("Project Status:", project.status)

                print("--------------------")

        # SEARCH PROJECT

        elif choice == "6":

            if len(projects) == 0:

                print("No projects.")

                continue

            project_id = int(input("Enter project ID: "))

            found = False

            for project in projects:

                if project.id == project_id:

                    print("\n===== PROJECT FOUND =====")

                    print("Project ID:", project.id)
                    print("Project Name:", project.name)
                    print("Project Description:", project.description)
                    print("Project Budget:", project.budget)
                    print("Project Status:", project.status)

                    found = True

                    break

            if not found:

                print("Project not found.")

        # UPDATE PROJECT STATUS

        elif choice == "7":

            project_id = int(
                input("Project ID for updating status: ")
            )

            found = False

            for project in projects:

                if project.id == project_id:

                    found = True

                    print("\n===== PROJECT =====")

                    print("Project ID:", project.id)
                    print("Project Name:", project.name)
                    print("Current Status:", project.status)

                    current_status = project.status.lower()

                    if current_status == "open":

                        print("\n1. In Progress")
                        print("2. Cancelled")

                        status_choice = input("Choose status: ")

                        if status_choice == "1":

                            new_status = "In Progress"

                        elif status_choice == "2":

                            new_status = "Cancelled"

                        else:

                            print("Invalid choice.")

                            break

                    elif current_status == "in progress":

                        print("\n1. Completed")
                        print("2. Cancelled")

                        status_choice = input("Choose status: ")

                        if status_choice == "1":

                            new_status = "Completed"

                        elif status_choice == "2":

                            new_status = "Cancelled"

                        else:

                            print("Invalid choice.")

                            break

                    elif current_status == "completed":

                        print("Project already completed.")

                        break

                    elif current_status == "cancelled":

                        print("Project already cancelled.")

                        break

                    else:

                        print("Invalid project status.")

                        break

                    project.status = new_status

                    with open("projects.txt", "w") as f:

                        for p in projects:

                            f.write(
                                f"{p.id}|"
                                f"{p.name}|"
                                f"{p.description}|"
                                f"{p.budget}|"
                                f"{p.status}\n"
                            )

                    print("Project status updated successfully.")

                    break

            if not found:

                print("Project not found.")

        # DELETE PROJECT

        elif choice == "8":

            if len(projects) == 0:

                print("Make sure to add a project first.")

                continue

            project_id = int(
                input("Enter project ID to delete: ")
            )

            found = False

            has_jobs = False

            for index, project in enumerate(projects):

                if project.id == project_id:

                    found = True

                    # Check whether this project has jobs

                    for job in jobs:

                        if job.project_id == project.id:

                            has_jobs = True

                            break

                    if has_jobs:

                        print(
                            "Cannot delete this project because "
                            "jobs already exist under it."
                        )

                        break

                    projects.pop(index)

                    # Reassign IDs

                    for index, p in enumerate(projects):

                        p.id = index + 1

                    # Rewrite file

                    with open("projects.txt", "w") as f:

                        for p in projects:

                            f.write(
                                f"{p.id}|"
                                f"{p.name}|"
                                f"{p.description}|"
                                f"{p.budget}|"
                                f"{p.status}\n"
                            )

                    print("Project deleted successfully.")

                    break

            if not found:

                print("Enter a valid project ID.")

        # CREATE JOB

        elif choice == "9":

            create_job(
                jobs,
                projects
            )

        # VIEW JOBS

        elif choice == "10":

            if len(jobs) == 0:

                print("No jobs available.")

                continue

            print("\n===== ALL JOBS =====")

            for job in jobs:

                print("Job ID:", job.id)
                print("Project ID:", job.project_id)
                print("Title:", job.title)
                print("Description:", job.description)
                print("Budget:", job.budget)
                print("Priority:", job.priority)
                print("Status:", job.status)
                print("Assigned To:", job.assigned_to)

                print("--------------------")

        # SEARCH JOB

        elif choice == "11":

            job_id = int(input("Enter job ID: "))

            found = False

            for job in jobs:

                if job.id == job_id:

                    print("\n===== JOB FOUND =====")

                    print("Job ID:", job.id)
                    print("Project ID:", job.project_id)
                    print("Title:", job.title)
                    print("Description:", job.description)
                    print("Budget:", job.budget)
                    print("Priority:", job.priority)
                    print("Status:", job.status)
                    print("Assigned To:", job.assigned_to)

                    found = True

                    break

            if not found:

                print("Job not found.")

        # UPDATE JOB STATUS

        elif choice == "12":

            job_id = int(input("Enter job ID: "))

            found = False

            for job in jobs:

                if job.id == job_id:

                    found = True

                    print("Current Status:", job.status)

                    current_status = job.status.lower()

                    if current_status == "open":

                        print("1. Cancelled")

                        status_choice = input("Choose: ")

                        if status_choice == "1":

                            job.status = "Cancelled"

                        else:

                            print("Invalid choice.")

                            break

                    elif current_status == "assigned":

                        print("1. Cancelled")

                        status_choice = input("Choose: ")

                        if status_choice == "1":

                            job.status = "Cancelled"

                        else:

                            print("Invalid choice.")

                            break

                    elif current_status == "in progress":

                        print("1. Cancelled")

                        status_choice = input("Choose: ")

                        if status_choice == "1":

                            job.status = "Cancelled"

                        else:

                            print("Invalid choice.")

                            break

                    elif current_status == "submitted":

                        print(
                            "Submitted jobs should be reviewed "
                            "through Submission Review."
                        )

                        break

                    elif current_status == "completed":

                        print("Job already completed.")

                        break

                    elif current_status == "cancelled":

                        print("Job already cancelled.")

                        break

                    elif current_status == "changes required":

                        print("User needs to work on this job again.")

                        break

                    else:

                        print("Invalid status.")

                        break

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

                    print("Job status updated.")

                    break

            if not found:

                print("Job not found.")

        # VIEW APPLICATIONS

        elif choice == "13":

            if len(applications) == 0:

                print("No applications.")

                continue

            print("\n===== APPLICATIONS =====")

            for application in applications:

                print("Application ID:", application.id)
                print("Job ID:", application.job_id)
                print("User ID:", application.user_id)
                print("Message:", application.message)
                print("Status:", application.status)

                print("--------------------")

        # APPROVE APPLICATION

        elif choice == "14":

            application_id = int(
                input("Enter application ID: ")
            )

            found = False

            for application in applications:

                if application.id == application_id:

                    found = True

                    if application.status != "Pending":

                        print("Only pending applications can be approved.")

                        break

                    selected_job = None

                    for job in jobs:

                        if job.id == application.job_id:

                            selected_job = job

                            break

                    if selected_job is None:

                        print("Job not found.")

                        break

                    if selected_job.status != "Open":

                        print("This job is no longer available.")

                        break

                    application.status = "Approved"

                    selected_job.status = "Assigned"

                    selected_job.assigned_to = application.user_id

                    # Reject other applications

                    for other_application in applications:

                        if (other_application.job_id == selected_job.id and other_application.id != application.id and other_application.status == "Pending" ):

                            other_application.status = "Rejected"

                    # Save applications

                    with open("applications.txt", "w") as f:

                        for a in applications:

                            f.write(
                                f"{a.id}|"
                                f"{a.job_id}|"
                                f"{a.user_id}|"
                                f"{a.message}|"
                                f"{a.status}\n"
                            )

                    # Save jobs

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

                    print("Application approved.")
                    print("Job assigned to user.")

                    break

            if not found:

                print("Application not found.")

        # REJECT APPLICATION

        elif choice == "15":

            application_id = int(input("Enter application ID: "))

            found = False

            for application in applications:

                if application.id == application_id:

                    found = True

                    if application.status != "Pending":

                        print(
                            "Only pending applications can be rejected."
                        )

                        break

                    application.status = "Rejected"

                    with open("applications.txt", "w") as f:

                        for a in applications:

                            f.write(
                                f"{a.id}|"
                                f"{a.job_id}|"
                                f"{a.user_id}|"
                                f"{a.message}|"
                                f"{a.status}\n"
                            )

                    print("Application rejected.")

                    break

            if not found:

                print("Application not found.")

        # VIEW SUBMISSIONS

        elif choice == "16":

            if len(submissions) == 0:

                print("No submissions.")

                continue

            print("\n===== SUBMISSIONS =====")

            for submission in submissions:

                print("Submission ID:", submission.id)
                print("Job ID:", submission.job_id)
                print("User ID:", submission.user_id)
                print("Work:", submission.work)
                print("Status:", submission.status)

                print("--------------------")

        # REVIEW SUBMISSION

        elif choice == "17":

            submission_id = int(input("Enter submission ID: "))

            found = False

            for submission in submissions:

                if submission.id == submission_id:

                    found = True

                    print("\n===== SUBMISSION =====")

                    print("Submission ID:", submission.id)
                    print("Job ID:", submission.job_id)
                    print("User ID:", submission.user_id)
                    print("Work:", submission.work)
                    print("Status:", submission.status)

                    if submission.status != "Submitted":

                        print("Only submitted work can be reviewed.")

                        break

                    print("\n1. Approve")
                    print("2. Request Changes")
                    print("3. Reject")

                    review_choice = input("Choose: ")

                    selected_job = None

                    for job in jobs:

                        if job.id == submission.job_id:

                            selected_job = job

                            break

                    if selected_job is None:

                        print("Job not found.")

                        break

                    if review_choice == "1":

                        submission.status = "Approved"

                        selected_job.status = "Completed"

                        print("Submission approved.")
                        print("Job completed.")

                    elif review_choice == "2":

                        submission.status = "Changes Required"

                        selected_job.status = "Changes Required"

                        print("Changes requested.")

                    elif review_choice == "3":

                        submission.status = "Rejected"

                        selected_job.status = "Cancelled"

                        print("Submission rejected.")
                        print("Job cancelled.")

                    else:

                        print("Invalid choice.")

                        break

                    # Save submissions

                    with open("submissions.txt", "w") as f:

                        for s in submissions:

                            f.write(
                                f"{s.id}|"
                                f"{s.job_id}|"
                                f"{s.user_id}|"
                                f"{s.work}|"
                                f"{s.status}\n"
                            )

                    # Save jobs

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

                    break

            if not found:

                print("Submission not found.")

        # REPORTS

        elif choice == "18":

            print("\n========================")
            print("        REPORTS")

            # Users

            total_users = len(users)
            active_users = 0
            inactive_users = 0

            for user in users:

                if user.status == "Active":

                    active_users += 1

                else:

                    inactive_users += 1

            # Projects

            total_projects = len(projects)
            open_projects = 0
            in_progress_projects = 0
            completed_projects = 0
            cancelled_projects = 0

            for project in projects:

                if project.status == "Open":

                    open_projects += 1

                elif project.status == "In Progress":

                    in_progress_projects += 1

                elif project.status == "Completed":

                    completed_projects += 1

                elif project.status == "Cancelled":

                    cancelled_projects += 1

            # Jobs

            total_jobs = len(jobs)

            job_status_count = {
                "Open": 0,
                "Assigned": 0,
                "In Progress": 0,
                "Submitted": 0,
                "Completed": 0,
                "Cancelled": 0,
                "Changes Required": 0
            }

            for job in jobs:

                if job.status in job_status_count:

                    job_status_count[job.status] += 1

            # Applications

            pending_applications = 0
            approved_applications = 0
            rejected_applications = 0

            for application in applications:

                if application.status == "Pending":

                    pending_applications += 1

                elif application.status == "Approved":

                    approved_applications += 1

                elif application.status == "Rejected":

                    rejected_applications += 1

            # Submissions

            total_submissions = len(submissions)
            approved_submissions = 0
            changes_submissions = 0
            rejected_submissions = 0

            for submission in submissions:

                if submission.status == "Approved":

                    approved_submissions += 1

                elif submission.status == "Changes Required":

                    changes_submissions += 1

                elif submission.status == "Rejected":

                    rejected_submissions += 1

            print("\n----- USERS -----")

            print("Total Users:", total_users)
            print("Active Users:", active_users)
            print("Inactive Users:", inactive_users)

            print("\n----- PROJECTS -----")

            print("Total Projects:", total_projects)
            print("Open:", open_projects)
            print("In Progress:", in_progress_projects)
            print("Completed:", completed_projects)
            print("Cancelled:", cancelled_projects)

            print("\n----- JOBS -----")

            print("Total Jobs:", total_jobs)

            for status, count in job_status_count.items():

                print(status + ":", count)

            print("\n----- APPLICATIONS -----")

            print("Pending:", pending_applications)
            print("Approved:", approved_applications)
            print("Rejected:", rejected_applications)

            print("\n----- SUBMISSIONS -----")

            print("Total Submissions:", total_submissions)
            print("Approved:", approved_submissions)
            print("Changes Required:", changes_submissions)
            print("Rejected:", rejected_submissions)

        # LOGOUT

        elif choice == "19":

            print("Logged out.")

            return

        # BACK

        elif choice == "20":

            return

        else:

            print("Invalid choice.")