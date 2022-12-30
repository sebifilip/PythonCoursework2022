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
        print("""
        1. Recommend friends
        2. Display common friends
        3. Display number of friends
        4. Display least number of friends
        5. Display list of friends
        6. Display indirect friendships
        7. Quit
        """)
        while True:
            choice = input("Please enter a number, 1 to 7: ")
            if choice == "1":
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
        :return: None
        """
        while True:
            if exists(file_name):
                social_NW: SocialNetwork = Loader.load_network(file_name)
                disp_network: str = input("Display the social network (y/n)? ")
                if disp_network == "n":
                    break
                elif disp_network == "y":
                    Printer.display_network(social_NW)
                    Runner.menu(social_NW)
                else:
                    Printer.display_invalid_input()
            elif file_name == "n":
                break
            else:
                print("Sorry, could not open file!")
                file_name = input("Enter a file name for network data: ")

    @staticmethod
    def recommend_friends(network: SocialNetwork):
        while True:
            user_name = input("Enter a username: ")
            if user_name not in network.users:
                Printer.display_nonexistent_user()
            else:
                Printer.display_recommended_friend(network, user_name)
                another = input("Do you want to recommend friends to another user (y/n)? ")
                if another == "y":
                    user_name = input("Enter a username: ")
                    if user_name not in network.users:
                        Printer.display_nonexistent_user()
                    else:
                        Printer.display_recommended_friend(network, user_name)
                        another = input("Do you want to recommend friends to another user (y/n)? ")
                        if another == "y":
                            pass
                        elif another == "n":
                            break
                        else:
                            Printer.display_invalid_input()
                elif another == "n":
                    break
                else:
                    Printer.display_invalid_input()

    @staticmethod
    def common_friends(network: SocialNetwork):
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
    def num_of_friends(network):
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
    def least_friends(network):
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
    def list_of_friends(network):
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
    def indirect_friends(network):
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
        while True:
            another_network = input("Do you want to try another network? ")
            if another_network == "y":
                Runner.run_program(input("Enter a file name for network data: "))
            elif another_network == "n":
                sys.exit()
            else:
                Printer.display_invalid_input()
