from os.path import exists
from user import User
from social_network import SocialNetwork


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
                line = line.strip()
                if i > 0:
                    connection: list[str] = line.split()
                    if len(connection) == 1:
                        user_name: str = connection[0]
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
        all_users: dict[str, User] = data.users
        for user_name in all_users:
            user_friends: list[User] = data.get_friends(user_name)
            friend_names: list[str] = []
            for friend in user_friends:
                friend_names += [friend.name]
            friend_names_str: str = ", ".join(friend_names)
            print(f"{user_name} -> {friend_names_str}")


class Runner:
    """
    Runs the program.
    """
    @staticmethod
    def run(file_name: str):
        """
        Starts running the program.
        :param file_name: name of the .txt file to open and load.
        :return: None
        """
        if exists(file_name):
            social_NW: SocialNetwork = Loader.load(file_name)
            disp: str = input("Display the social network (y/n)? ")
            if disp == "n":
                pass
            elif disp == "y":
                Printer.display(social_NW)
            else:
                print("Invalid input!")
        elif file_name == "n":
            pass
        else:
            print("Sorry, could not open file!")


print("Social network simulator.")
Runner.run(input("Enter a file name for network data: "))
while True:
    another_network = input("Do you want to try another network? ")
    if another_network == "y":
        Runner.run(input("Enter a file name for network data: "))
    elif another_network == "n":
        break
    else:
        print("Invalid input!")
