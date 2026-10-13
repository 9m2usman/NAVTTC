class Job:

    def __init__(self,job_id,project_id,title,description,budget,priority="Medium",status="Open",assigned_to=None):

        self.id = job_id
        self.project_id = project_id
        self.title = title
        self.description = description
        self.budget = budget
        self.priority = priority
        self.status = status
        self.assigned_to = assigned_to