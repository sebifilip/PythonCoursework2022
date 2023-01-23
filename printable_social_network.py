from social_network import SocialNetwork
from printer import Printer
from typing import Optional


class PrintableSocialNetwork(SocialNetwork):
    """
    Prints the social network to the console.
    """
    _printer: Printer

    def __init__(self, printer: Printer, data: Optional[SocialNetwork] = None):
        """
        Initialises the social network to print.
        :param printer: Printer instance where teh social network is printed to.
        :param data: social network data.
        """
        SocialNetwork.__init__(self)
        self._printer = printer
        self._data = self if data is None else data

    def display_network(self):
        """
        Pretty prints the social network on the Python terminal.
        :return: None.
        """
        self._printer.display_network(self._data)

    def display_common_friends(self):
        """
        Pretty prints the number of common friends per pair of users.
        :return: None.
        """
        self._printer.display_common_friends(self._data)

    def display_recommended_friend(self, user_name: str):
        """
        Prints the friend recommendation for a given user.
        :param user_name: name of the user seeking a new friend.
        :return: None.
        """
        self._printer.display_recommended_friend(self._data, user_name)

    def display_number_of_friends(self, user_name: str):
        """
        Prints the number of friends for a given user.
        :param user_name: name of the user to output its number of friends.
        :return: None.
        """
        self._printer.display_number_of_friends(self._data, user_name)

    def display_least_num_friends(self):
        """
        Prints the names of the users with less than 2 friends.
        :return: None.
        """
        self._printer.display_least_num_friends(self._data)

    def display_user_relationship(self, user_name: str):
        """
        Prints the username and their list of friends.
        :param user_name: name of the user to output.
        :return: None.
        """
        self._printer.display_user_relationship(self._data, user_name)

    def display_indirect_relationships(self):
        """
        Prints indirect relations of users.
        :return: None.
        """
        self._printer.display_indirect_relationships(self._data)
