from social_network import SocialNetwork, InconsistentException
from os.path import exists
from loader import Loader
from printer import Printer
from printable_social_network import PrintableSocialNetwork
import sys


class Runner:
    """
    Runs the program.
    """
    _loader: Loader
    _printer: Printer

    def __init__(self, loader: Loader, printer: Printer):
        """
        Initialises the Loader and Printer instances to run the program.
        :param loader: Loader instance to load the social network.
        :param printer: Printer instance to output the network.
        """
        self._loader = loader
        self._printer = printer

    # Feature 1 i.
    def run_program(self, file_name: str):
        """
        Starts running the program.
        :param file_name: name of the .txt file to open and load.
        :return: None.
        """
        while True:
            if file_name == "n":
                break
            elif exists(file_name):
                try:
                    social_nw: SocialNetwork = self._loader.load_network(file_name)
                except InconsistentException as e:
                    print(str(e))
                    file_name: str = input("Enter a file name for network data: ")
                else:
                    self.menu(social_nw)
            else:
                print("Sorry, could not open file!")
                file_name: str = input("Enter a file name for network data: ")

    def menu(self, data: SocialNetwork):
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
                self.show_network(data)
            elif choice == "1":
                self.recommend_friends(data)
            elif choice == "2":
                self.common_friends(data)
            elif choice == "3":
                self.num_of_friends(data)
            elif choice == "4":
                self.least_friends(data)
            elif choice == "5":
                self.list_of_friends(data)
            elif choice == "6":
                self.indirect_friends(data)
            elif choice == "7":
                self.another_network()
                break
            elif choice == "8":
                sys.exit()
            else:
                print("Invalid input!")

    # Feature 1 ii.
    def show_network(self, network: SocialNetwork):
        """
        Calls the display_network method to display the social network.
        :param network: list of users and their friends.
        :return: None.
        """
        PrintableSocialNetwork(self._printer, network).display_network()

    # Feature 2 ii.
    def recommend_friends(self, network: SocialNetwork):
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
                PrintableSocialNetwork(self._printer, network).display_recommended_friend(user_name)
                break

    # Feature 2 i.
    def common_friends(self, network: SocialNetwork):
        """
        Asks the user to enter a name and display a matrix of common friends between users.
        :param network: list of users and their friends.
        :return: None.
        """
        PrintableSocialNetwork(self._printer, network).display_common_friends()

    # Feature 3 i.
    def num_of_friends(self, network: SocialNetwork):
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
                PrintableSocialNetwork(self._printer, network).display_number_of_friends(user_name)
                break

    # Feature 3 ii.
    def least_friends(self, network: SocialNetwork):
        """
        Asks the user if they want to display the users with the least number of friends.
        :param network: list of users and their friends.
        :return: None.
        """
        PrintableSocialNetwork(self._printer, network).display_least_num_friends()

    # Feature 3 iii.
    def list_of_friends(self, network: SocialNetwork):
        """
        Asks the user to enter a name and display their friends.
        :param network: list of users and their friends.
        :return: None.
        """
        while True:
            user_name: str = input("Enter a username: ")
            if user_name not in network.users:
                print("User not found!")
            else:
                PrintableSocialNetwork(self._printer, network).display_user_relationship(user_name)
                break

    # Feature 3 iv.
    def indirect_friends(self, network: SocialNetwork):
        """
        Asks the user to enter a name and display indirect friendships.
        :param network: list of users and their friends.
        :return: None.
        """
        PrintableSocialNetwork(self._printer, network).display_indirect_relationships()

    def another_network(self):
        """
        ASks the user if they want to try another social network.
        :return: None.
        """
        Runner(self._loader, self._printer).run_program(input("Enter a file name for network data: "))
