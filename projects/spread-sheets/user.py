class User:
    def __init__(self,email,name,job,password):
        self.email = email
        self.name = name
        self.job = job
        self.password = password
        
    def change_password(self,new_password):
        self.password = new_password
     
    def get_user_info(self):
        print(f"User {self.email} currently works as {self.job} ")
        