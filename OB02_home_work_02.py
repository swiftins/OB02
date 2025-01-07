class User:
    def __init__(self, user_id, name, access_level='user'):
        self._user_id = user_id  
        self._access_level = access_level  

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name

    def set_access_level(self, access_level):
        self._access_level = access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, access_level='admin')
        self._users = []  

    def add_user(self, user):
        if isinstance(user, User):
            self._users.append(user)
            print(f"User {user.get_name()} added.")
        else:
            print("Error: Only instances of User can be added.")

    def remove_user(self, user):
        if user in self._users:
            self._users.remove(user)
            print(f"User {user.get_name()} removed.")
        else:
            print(f"User {user.get_name()} not found in the system.")

    def list_users(self):
        if self._users:
            print("Current users in the system:")
            for user in self._users:
                print(f"- ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")
        else:
            print("No users in the system.")


