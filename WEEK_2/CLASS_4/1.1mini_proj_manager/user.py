class User:
    def __init__(self,user_id,name,email,password,role="User",status="Active"):
        self.id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.status = status