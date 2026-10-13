class Submission:

    def __init__(self,submission_id,job_id,user_id,work,status="Submitted"):

        self.id = submission_id
        self.job_id = job_id
        self.user_id = user_id
        self.work = work
        self.status = status