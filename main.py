from os.path import exists
from social_network import SocialNetwork
from printer import Printer


class Loader:
    """
    Opens and reads a .txt file of social network of users.
    """
    @staticmethod
    def load_network(data_file_name: str) -> SocialNetwork:
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
            social_NW: SocialNetwork = Loader.load_network(file_name)
            disp_network: str = input("Display the social network (y/n)? ")
            if disp_network == "n":
                pass
            elif disp_network == "y":
                Printer.display_network(social_NW)
                while True:
                    while True:
                        user_name = input("Enter a username: ")
                        if user_name not in social_NW.users:
                            print("Username not found!")
                        else:
                            break
                    Printer.display_recommended_friend(social_NW, user_name)
                    another = input("Do you want to recommend friends to another user (y/n)? ")
                    if another == "y":
                        pass
                    elif another == "n":
                        break
                    else:
                        print("Invalid input!")
            else:
                print("Invalid input!")

            disp_cf: str = input("Display common friends matrix (y/n)? ")
            if disp_cf == "n":
                pass
            elif disp_cf == "y":
                Printer.display_common_friends(social_NW)

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
