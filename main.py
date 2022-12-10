from os.path import exists
from typing import Optional


class User:
    """
    Encapsulation of a user with the names of its friends.
    """
    name: str
    friend_names: list[str]

    def __init__(self, user_name: str):
        """
        Initialises the user object with an empty list of friend names.
        :param user_name: name of the user.
        """
        self.name = user_name
        self.friend_names = []

    def add_friend(self, friend_name: str):
        """
        Adds a name to the list of friend names.
        :param friend_name: name of the friend to add.
        :return: None
        """
        self.friend_names += friend_name


class SocialNetwork:
    """
    Encapsulation of the users and their friends.
    """
    users: dict[str, User]

    def __init__(self):
        """
        Initialises the map of users to empty.
        """
        self.users = {}

    def add_user(self, user_name: str) -> User:
        """
        Adds a user to the network if it does not exist.
        :param user_name: name of the user to add.
        :return: user object corresponding to the given name.
        """
        if user_name not in self.users:
            self.users[user_name] = User(user_name)
        return self.users[user_name]

    def add_friend(self, user_name: str, friend_name: str) -> User:
        """
        Associates a user to a new friend.
        :param user_name: name of user to associate.
        :param friend_name: name of friend to associate with.
        :return: user object corresponding to a friend.
        """
        user: User = self.add_user(user_name)
        friend: User = self.add_user(friend_name)
        user.add_friend(friend_name)
        friend.add_friend(user_name)
        return friend

    def get_user(self, user_name: str) -> Optional[User]:
        """
        Gets the user associated with given name, if any.
        :param user_name: name of user to get.
        :return: user object corresponding to the name or None.
        """
        if user_name in self.users:
            return self.users[user_name]
        return None

    def get_friends(self, user_name: str) -> list[User]:
        """
        Gets the list of objects corresponding to the friends of the given user.
        :param user_name: name of user to get friends of, if any.
        :return: list of friend objects or empty list if user does not exist.
        """
        user: User = self.get_user(user_name)
        if user is None:
            return []
        result: list[User] = []
        for friend_name in user.friend_names:
            friend: User = self.get_user(friend_name)
            result += friend
        return result


class Loader:
    """
    Opens and reads a .txt file of social network of users.
    """
    @staticmethod
    def load(data_file_name: str) -> SocialNetwork:
        """
        Opens the data file, reads the users and returns the social network.
        :param data_file_name: name of the data file to open and read.
        :return: social network object.
        """
        sn: SocialNetwork = SocialNetwork()
        i = 0
        with open(data_file_name, "r") as reader:
            for line in reader.readlines():
                if i > 0:
                    connection: list[str] = line.split()
                    if len(connection) == 1:
                        sn.add_user(user_name)
                    elif len(connection) == 2:
                        user_name, friend_name = connection
                        sn.add_friend(user_name, friend_name)
                    else:
                        raise ValueError("Social network line does not have one or two elements: " + line)
                i += 1
        return sn


class Printer:
    """
    Displays the social network on the Python console.
    """
    @staticmethod
    def display(data: SocialNetwork):
        """
        Pretty prints the social network on the Python terminal.
        :param data: list of users and their friends to output.
        :return: None.
        """
        all_users: dict[str, User.friend_names] = data.users
        for user_name in all_users:
            print(f"{user_name} -> {all_users[user_name]}")


class Runner:
    """
    Runs the program.
    """
    @staticmethod
    def run(file_name):
        """
        Starts running the program.
        :param file_name: name of the .txt file to open and load.
        :return: None
        """
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
