from social_network import SocialNetwork
from printer import Printer
from os.path import exists
from loader import Loader
import sys


class Runner:
    """
    Runs the program.
    """
    @staticmethod
    def menu(data: SocialNetwork):
        """
        Displays a menu of choices to make the program more intuitive.
        :param data: list of users and their friends.
        :return: None.
        """
        print("""
        0. Display network
        1. Recommend friends
        2. Display common friends
        3. Display number of friends
        4. Display least number of friends
        5. Display list of friends
        6. Display indirect friendships
        7. Quit
        """)
        while True:
            choice = input("Please enter a number, 0 to 7: ")
            if choice == "0":
                Runner.show_network(data)
            elif choice == "1":
                Runner.recommend_friends(data)
            elif choice == "2":
                Runner.common_friends(data)
            elif choice == "3":
                Runner.num_of_friends(data)
            elif choice == "4":
                Runner.least_friends(data)
            elif choice == "5":
                Runner.list_of_friends(data)
            elif choice == "6":
                Runner.indirect_friends(data)
            elif choice == "7":
                Runner.another_network()
            else:
                Printer.display_invalid_input()

    @staticmethod
    def run_program(file_name: str):
        """
        Starts running the program.
        :param file_name: name of the .txt file to open and load.
        :return: None.
        """
        while True:
            if exists(file_name):
                social_NW: SocialNetwork = Loader.load_network(file_name)
                Runner.menu(social_NW)
            elif file_name == "n":
                break
            else:
                print("Sorry, could not open file!")
                file_name: str = input("Enter a file name for network data: ")

    @staticmethod
    def show_network(data: SocialNetwork):
        while True:
            disp_network: str = input("Display the social network (y/n)? ")
            if disp_network == "n":
                break
            elif disp_network == "y":
                Printer.display_network(data)
                break
            else:
                Printer.display_invalid_input()

    @staticmethod
    def recommend_friends(network: SocialNetwork):
        """
        Asks the user if they want to recommend friends and to enter a name.
        :param network: list of users and their friends.
        :return: None.
        """
        while True:
            user_name: str = input("Enter a username: ")
            if user_name not in network.users:
                Printer.display_nonexistent_user()
            else:
                Printer.display_recommended_friend(network, user_name)
                another: str = input("Do you want to recommend friends to another user (y/n)? ")
                if another == "y":
                    pass
                elif another == "n":
                    break
                else:
                    Printer.display_invalid_input()

    @staticmethod
    def common_friends(network: SocialNetwork):
        """
        Asks the user to enter a name and display a matrix of common friends between users.
        :param network: list of users and their friends.
        :return: None.
        """
        while True:
            disp_cf: str = input("Display common friends matrix (y/n)? ")
            if disp_cf == "n":
                break
            elif disp_cf == "y":
                Printer.display_common_friends(network)
                break
            else:
                Printer.display_invalid_input()

    @staticmethod
    def num_of_friends(network: SocialNetwork):
        """
        Asks the user to enter a name and display the number of friends.
        :param network: list of users and their friends.
        :return: None.
        """
        while True:
            disp_num: str = input("Display how many friends a user has (y/n)? ")
            if disp_num == "n":
                break
            elif disp_num == "y":
                user_name: str = input("Enter a user name: ")
                if user_name not in network.users:
                    Printer.display_nonexistent_user()
                else:
                    Printer.display_number_of_friends(network, user_name)
                    break
            else:
                Printer.display_invalid_input()

    @staticmethod
    def least_friends(network: SocialNetwork):
        """
        Asks the user if they want to display the users with the least number of friends.
        :param network: list of users and their friends.
        :return: None.
        """
        while True:
            disp_least: str = input("Display the users with the least number of or have 0 friends (y/n)? ")
            if disp_least == "n":
                break
            elif disp_least == "y":
                Printer.display_least_num_friends(network)
                break
            else:
                Printer.display_invalid_input()

    @staticmethod
    def list_of_friends(network: SocialNetwork):
        """
        Asks the user to enter a name and display their friends.
        :param network: list of users and their friends.
        :return: None.
        """
        while True:
            disp_least: str = input("Display the list of friends for a user (y/n)? ")
            if disp_least == "n":
                break
            elif disp_least == "y":
                user_name: str = input("Enter a user name: ")
                if user_name not in network.users:
                    Printer.display_nonexistent_user()
                else:
                    Printer.display_user_relationship(network, user_name)
                    break
            else:
                Printer.display_invalid_input()

    @staticmethod
    def indirect_friends(network: SocialNetwork):
        """
        Asks the user to enter a name and display indirect friendships.
        :param network: list of users and their friends.
        :return: None.
        """
        while True:
            disp_indirect: str = input("Display the friends of the friends of a given user (y/n)? ")
            if disp_indirect == "n":
                break
            elif disp_indirect == "y":
                Printer.display_indirect_relationships(network)
                break
            else:
                Printer.display_invalid_input()

    @staticmethod
    def another_network():
        """
        ASks the user if they want to try another social network.
        :return: None.
        """
        while True:
            another_network: str = input("Do you want to try another network? ")
            if another_network == "y":
                Runner.run_program(input("Enter a file name for network data: "))
            elif another_network == "n":
                sys.exit()
            else:
                Printer.display_invalid_input()
