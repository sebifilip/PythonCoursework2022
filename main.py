from os.path import exists


class User:

    def __init__(self, name, friends):
        self.friends = friends
        self.name = name

    def constructor(self, user_name):
        self.name = user_name

    def add_friend(self, friend):
        self.friends += friend


class SocialNetwork:

    def __init__(self, users):
        self.users = users

    def add_user(self, user_name):
        if user_name in self.users:
            self.users[user_name] = ""
        return User(user_name)

    def add_friend(self, user_name, friend_name):
        self.users[user_name] = friend_name
        return User(user_name, friend_name)

    def get_user(self, user_name):
        if user_name in self.users:
            user = User(user_name.name, user_name.friends)
            return user.name
        return None

    def get_friends(self, user_name):
        user = User(user_name.name, user_name.friends)
        return user.friends


class Loader:

    def load(self, data_file_name):
        if exists(data_file_name):
            data = open(data_file_name, "r")
        else:
            print("Sorry, could not open file!")
        social_NW = SocialNetwork({})
        lines = data.readlines()
        for l in lines:
            connection = l.split(" ")
            for u in connection:
                user = User(u, [])
                social_NW.add_user(user)


class Printer:

    def display(self, data):
        for user in data:
            print(f"{user.get_user(user)} -> {user.get_friends(data[user])}")


class Runner:

    def run(self, file_name):
        self.file_name = file_name
        print("Social network simulator.")
        load = Loader()
        load.load(self.file_name)
        disp = input("Display the social network (y/n)? ")
        if disp == "n":
            pass
        elif disp == "y":
            disp = Printer(SocialNetwork())
            disp.display(self.file_name)


program = Runner()
program.run(input("Enter a file name for network data: "))
