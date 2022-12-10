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
        if user_name not in self.users:
            self.users[user_name] = ""
        return User(user_name, "")

    def add_friend(self, user_name, friend_name):
        self.users[user_name] = friend_name
        return User(user_name, friend_name)

    def get_user(self, user_name):
        if user_name in self.users:
            user = User(user_name.name, user_name.friends)
            return user.name
        return None

    def get_friends(self, user_name):
        user = User(user_name, user_name.friends)
        return user.friends


class Loader:

    def load(self, data_file_name):
        social_NW = {}
        social_NW_ins = SocialNetwork(social_NW)
        i = 0
        with open(data_file_name, "r") as reader:
            for line in reader.readlines():
                connection = line.split(" ")
                if i > 0:
                    for u in connection:
                        social_NW_ins.add_user(u)
        print(social_NW)
        return social_NW


class Printer:

    def display(self, data):
        users = Loader()
        users.load(data)
        for u in data:
            print(f"->")


class Runner:

    def run(self, file_name):
        if exists(file_name):
            load = Loader()
            load.load(file_name)
            disp = input("Display the social network (y/n)? ")
            if disp == "n":
                pass
            elif disp == "y":
                disp = Printer()
                disp.display(file_name)
        else:
            print("Sorry, could not open file!")
            return None


program = Runner()
print("Social network simulator.")
program.run(input("Enter a file name for network data: "))
