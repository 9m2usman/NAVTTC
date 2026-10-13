from application import Application

def load_applications():

    applications = []

    try:

        with open("applications.txt", "r") as f:

            for line in f:

                line = line.strip()

                if line == "":
                    continue

                data = line.split("|")

                application_id = int(data[0])
                job_id = int(data[1])
                user_id = int(data[2])
                message = data[3]
                status = data[4]

                application = Application(application_id,job_id,user_id,message,status)

                applications.append(application)

    except FileNotFoundError:

        print("applications.txt not found. Starting with empty applications.")

    return applications