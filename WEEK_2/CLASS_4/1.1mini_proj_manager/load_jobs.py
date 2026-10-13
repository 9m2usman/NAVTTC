from job import Job

def load_jobs():

    jobs = []

    try:

        with open("jobs.txt", "r") as f:

            for line in f:

                line = line.strip()

                if line == "":
                    continue

                data = line.split("|")

                job_id = int(data[0])
                project_id = int(data[1])
                title = data[2]
                description = data[3]
                budget = float(data[4])
                priority = data[5]
                status = data[6]

                if data[7] == "None":

                    assigned_to = None

                else:

                    assigned_to = int(data[7])

                job = Job(job_id,project_id,title,description,budget,priority,status,assigned_to)

                jobs.append(job)

    except FileNotFoundError:

        print("jobs.txt not found. Starting with empty jobs.")

    return jobs