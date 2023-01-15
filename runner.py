from social_network import SocialNetwork
from console_printer import ConsolePrinter
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
        while True:
            print("""
====================================
0. Display network
1. Recommend friends
2. Display common friends
3. Display number of friends
4. Display least number of friends
5. Display list of friends
6. Display indirect friendships
7. Quit network
8. Quit program
====================================
            """)
            choice = input("Please enter a number, 0 to 8: ")
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
            elif choice == "8":
                sys.exit()
            else:
                print("Invalid input!")

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
    def show_network(network: SocialNetwork):
        """
        Calls the display_network method to display the social network.
        :param network: list of users and their friends.
        :return: None.
        """
        ConsolePrinter.display_network(network)

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
                print("Username does not exist!")
            else:
                ConsolePrinter.display_recommended_friend(network, user_name)
                break

    @staticmethod
    def common_friends(network: SocialNetwork):
        """
        Asks the user to enter a name and display a matrix of common friends between users.
        :param network: list of users and their friends.
        :return: None.
        """
        ConsolePrinter.display_common_friends(network)

    @staticmethod
    def num_of_friends(network: SocialNetwork):
        """
        Asks the user to enter a name and display the number of friends.
        :param network: list of users and their friends.
        :return: None.
        """
        while True:
            user_name: str = input("Enter a username: ")
            if user_name not in network.users:
                print("Username does not exist!")
            else:
                ConsolePrinter.display_number_of_friends(network, user_name)
                break

    @staticmethod
    def least_friends(network: SocialNetwork):
        """
        Asks the user if they want to display the users with the least number of friends.
        :param network: list of users and their friends.
        :return: None.
        """
        ConsolePrinter.display_least_num_friends(network)

    @staticmethod
    def list_of_friends(network: SocialNetwork):
        """
        Asks the user to enter a name and display their friends.
        :param network: list of users and their friends.
        :return: None.
        """
        while True:
            user_name: str = input("Enter a username: ")
            if user_name not in network.users:
                ConsolePrinter.display_nonexistent_user()
            else:
                ConsolePrinter.display_user_relationship(network, user_name)
                break

    @staticmethod
    def indirect_friends(network: SocialNetwork):
        """
        Asks the user to enter a name and display indirect friendships.
        :param network: list of users and their friends.
        :return: None.
        """
        ConsolePrinter.display_indirect_relationships(network)

    @staticmethod
    def another_network():
        """
        ASks the user if they want to try another social network.
        :return: None.
        """
        Runner.run_program(input("Enter a file name for network data: "))
