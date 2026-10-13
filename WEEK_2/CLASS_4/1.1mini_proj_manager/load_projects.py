from project import Project

def load_projects():

    projects = []

    try:

        with open("projects.txt", "r") as f:

            for line in f:

                line = line.strip()

                if line == "":
                    continue

                data = line.split("|")

                project_id = int(data[0])
                name = data[1]
                description = data[2]
                budget = float(data[3])
                status = data[4]

                project = Project(project_id,name,description,budget,status)

                projects.append(project)

    except FileNotFoundError:

        print("projects.txt not found. Starting with empty projects.")

    return projects