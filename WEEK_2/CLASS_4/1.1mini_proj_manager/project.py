class Project:
    def __init__(self,id,name,description,budget,status="open"):
        self.id = id
        self.name = name
        self.description = description
        self.budget = budget
        self.status = status