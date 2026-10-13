from project import Project

def create_project(projects):

    print("\n=====CREATE PROJECT=====")

    name = input("Enter project name: ")
    description = input("Enter project description: ")
    budget = float(input("Enter project budget: "))

    project_id = len(projects) + 1

    new_project = Project(project_id,name,description,budget)

    projects.append(new_project)

    with open("projects.txt", "a") as f:

        f.write(
            f"{new_project.id}|"
            f"{new_project.name}|"
            f"{new_project.description}|"
            f"{new_project.budget}|"
            f"{new_project.status}\n"
        )

    print("Project created successfully.")