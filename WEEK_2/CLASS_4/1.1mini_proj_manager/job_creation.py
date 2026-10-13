from job import Job

def create_job(jobs, projects):

    if len(projects) == 0:

        print("Create a project first.")

        return

    print("\n===== CREATE JOB =====")

    project_id = int(input("Enter project ID: "))

    project_found = False

    for project in projects:

        if project.id == project_id:

            project_found = True

            print("Project:", project.name)

            break

    if not project_found:

        print("Project not found.")

        return

    if project.status == "Completed":

        print("Cannot create job in completed project.")

        return

    if project.status == "Cancelled":

        print("Cannot create job in cancelled project.")

        return

    title = input("Enter job title: ")
    description = input("Enter job description: ")
    budget = float(input("Enter job budget: "))

    print("\nPriority")
    print("1. Low")
    print("2. Medium")
    print("3. High")
    print("4. Urgent")

    priority_choice = input("Choose priority: ")

    if priority_choice == "1":

        priority = "Low"

    elif priority_choice == "2":

        priority = "Medium"

    elif priority_choice == "3":

        priority = "High"

    elif priority_choice == "4":

        priority = "Urgent"

    else:

        print("Invalid priority.")

        return

    job_id = len(jobs) + 1

    new_job = Job(job_id,project_id,title,description,budget,priority)

    jobs.append(new_job)

    with open("jobs.txt", "a") as f:

        f.write(
            f"{new_job.id}|"
            f"{new_job.project_id}|"
            f"{new_job.title}|"
            f"{new_job.description}|"
            f"{new_job.budget}|"
            f"{new_job.priority}|"
            f"{new_job.status}|"
            f"{new_job.assigned_to}\n"
        )

    print("Job created successfully.")