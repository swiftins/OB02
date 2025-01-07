class User:
    def __init__(self, user_id, name, access_level='user'):
        self.user_id = user_id
        self.name = name
        self.access_level = access_level

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, access_level='admin')
        self.users = []

    def add_user(self, user):
        if isinstance(user, User):
            self.users.append(user)
            print(f"User {user.name} added.")
        else:
            print("Error: Only instances of User can be added.")

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f"User {user.name} removed.")
        else:
            print(f"User {user.name} not found in the system.")

    def list_users(self):
        if self.users:
            print("Current users in the system:")
            for user in self.users:
                print(f"- ID: {user.user_id}, Name: {user.name}, Access Level: {user.access_level}")
        else:
            print("No users in the system.")


if __name__ == "__main__":
    admin = Admin(user_id=1, name="Admin1")
    user1 = User(user_id=2, name="Tim")
    user2 = User(user_id=3, name="Din")

    admin.add_user(user1)
    admin.add_user(user2)
    admin.list_users()

    admin.remove_user(user1)
    admin.list_users()
