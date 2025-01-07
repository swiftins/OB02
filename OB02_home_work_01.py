class User:
    def __init__(self, user_ID, name, access_level="user"):
        self.user_ID = user_ID
        self.name = name
        self.access_level = access_level

class Admin(User):
    def __init__(self, user_ID, name):
        super().__init__(user_ID, name, access_level="admin")
        self.users = []

    def add_user(self, user):
        try:
            self.users.append(user)
            print(f"User {user.name} added.")
        except AttributeError:
            print("Invalid user object. Cannot add.")

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f"User {user.name} removed.")
        else:
            print(f"{user.name} not found in the list.")


admin = Admin(user_ID=1, name="Admin")
user1 = User(user_ID=2, name="User1")
user2 = User(user_ID=3, name="User2")

admin.add_user(user1)  
admin.remove_user(user1)  
admin.remove_user(user1) 
