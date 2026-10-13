from submission import Submission

def submit_work(submissions, jobs, current_user):

    print("\n===== SUBMIT WORK =====")

    job_id = int(input("Enter job ID: "))

    found_job = False

    for job in jobs:

        if job.id == job_id:

            found_job = True

            if job.assigned_to != current_user.id:

                print("This job is not assigned to you.")

                return

            if job.status != "In Progress":

                print("Job must be In Progress before submission.")

                return

            break

    if not found_job:

        print("Job not found.")

        return

    work = input("Describe your completed work: ")

    submission_id = len(submissions) + 1

    new_submission = Submission(submission_id,job_id,current_user.id,work)

    submissions.append(new_submission)

    with open("submissions.txt", "a") as f:

        f.write(
            f"{new_submission.id}|"
            f"{new_submission.job_id}|"
            f"{new_submission.user_id}|"
            f"{new_submission.work}|"
            f"{new_submission.status}\n"
        )

    job.status = "Submitted"

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

    print("Work submitted successfully.")