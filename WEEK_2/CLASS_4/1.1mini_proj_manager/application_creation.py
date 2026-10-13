from application import Application

def apply_for_job(applications, jobs, current_user):

    print("\n===== APPLY FOR JOB =====")

    if len(jobs) == 0:

        print("No jobs available.")

        return

    job_id = int(input("Enter job ID: "))

    found_job = False

    for job in jobs:

        if job.id == job_id:

            found_job = True

            if job.status != "Open":

                print("This job is not available.")

                return

            break

    if not found_job:

        print("Job not found.")

        return

    for application in applications:

        if (application.job_id == job_id and application.user_id == current_user.id):

            if application.status == "Pending":

                print("You already applied for this job.")

                return

            if application.status == "Approved":

                print("Your application was already approved.")

                return

    message = input("Enter application message: ")

    application_id = len(applications) + 1

    new_application = Application(application_id,job_id,current_user.id,message)

    applications.append(new_application)

    with open("applications.txt", "a") as f:

        f.write(
            f"{new_application.id}|"
            f"{new_application.job_id}|"
            f"{new_application.user_id}|"
            f"{new_application.message}|"
            f"{new_application.status}\n"
        )

    print("Application submitted successfully.")