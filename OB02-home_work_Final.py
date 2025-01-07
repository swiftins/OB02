class User:
    def __init__(self, user_ID, name):
        self.__user_ID = user_ID
        self.__name = name
        self.__access_level = "user"
    
    def get_user_ID(self):
        return self.__user_ID
    
    def get_name(self):
        return self.__name
    
    def get_access_level(self):
        return self.__access_level
    
    def set_name(self, name):
        self.__name = name
 
class Admin(User):
    def __init__(self, user_ID, name):
        super().__init__(user_ID, name)
        self.__access_level = "admin"
    
    def add_user(self, user_list, user):
        user_list.append(user)
        print(f"User {user.get_name()} added.")

    def remove_user(self, user_list, user):
        if user in user_list:
            user_list.remove(user)
            print(f"User {user.get_name()} removed.")
        else:
            print(f"User {user.get_name()} not listed.")

if __name__ == "__main__":
   
    user1 = User(1, "Tihonov")
    user2 = User(2, "Sidorov")
    
    admin = Admin(3, "Admin User")

    users = [user1, user2]

    new_user = User(4, "New User")
    admin.add_user(users, new_user)
   
    admin.remove_user(users, user1)

    for user in users:
        print(f"User {user.get_name()}, ID: {user.get_user_ID()}, Access Level: {user.get_access_level()}")


        



