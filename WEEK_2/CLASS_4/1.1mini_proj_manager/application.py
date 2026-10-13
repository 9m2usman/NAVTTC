class Application:

    def __init__(self,application_id,job_id,user_id,message,status="Pending"):

        self.id = application_id
        self.job_id = job_id
        self.user_id = user_id
        self.message = message
        self.status = status