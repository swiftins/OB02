class User():
    def __init__(self, user_ID, name, access_level = "user"):
        self.user_ID = user_ID
        self.name = name
        self.access_level = access_level
    
    
class Admin(User):
    def __init__(self, user_ID, name):
        super().__init__(user_ID, name, access_level = "admin")
        self.users = []
    
    def add_user(self, user):
        try:
            self.users.append(user)
            print(f"User {user.name} added.")
        
        except AttributeError:
    def remove_user(self, user):
        self.users.remove(user)
        if user in self.users
        else:
            print(f"{user.name} not found")


    





        

        