from submission import Submission


def load_submissions():

    submissions = []

    try:

        with open("submissions.txt", "r") as f:

            for line in f:

                line = line.strip()

                if line == "":
                    continue

                data = line.split("|")

                submission_id = int(data[0])
                job_id = int(data[1])
                user_id = int(data[2])
                work = data[3]
                status = data[4]

                submission = Submission(submission_id, job_id, user_id, work, status )

                submissions.append(submission)

    except FileNotFoundError:

        print("submissions.txt not found. Starting with empty submissions.")

    return submissions