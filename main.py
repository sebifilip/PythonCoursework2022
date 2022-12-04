from os.path import exists


class User:

    def __init__(self, name, friends):
        self.friends = friends
        self.name = name

    def constructor(self, user_name):
        name = self.user_name

    def add_friend(self, friend):
        friends = self.friend


class SocialNetwork:

    def __init__(self, users):
        self.users = users

    def add_user(self, user_name):
        self.users += user_name
        return User(user_name)

    def add_friend(self, user_name, friend_name):
        self.users[user_name] = friend_name
        return User(user_name, friend_name)

    def get_user(self, user_name):
        if self.user_name in dict.users:
            return User(user_name)
        return None

    def get_friends(self, user_name):
        return self.user_name


class Loader:

    def load(self, data_file_name):
        if exists(data_file_name):
            data = open(data_file_name, "r")
            return data
        else:
            print("Sorry, could not open file!")


class Printer:

    def display(self):
        pass


class Runner:

    def run(self, file_name):
        print("Social network simulator.")
        data = Printer()
        network = SocialNetwork({})


program = Runner()
program.run("nw_data.txt")
