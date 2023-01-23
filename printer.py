from social_network import SocialNetwork


class Printer:
    """
    Displays the social network.
    """
    def display_network(self, data: SocialNetwork):
        """
        Pretty prints the social network on the Python terminal.
        :param data: list of users and their friends to output.
        :return: None.
        """
        pass

    def display_common_friends(self, data: SocialNetwork):
        """
        Pretty prints the number of common friends per pair of users.
        :param data: list of users and number of common friends with each of the other users to output.
        :return: None.
        """
        pass

    def display_recommended_friend(self, data: SocialNetwork, user_name: str):
        """
        Prints the friend recommendation for a given user.
        :param data: list of users and their friends.
        :param user_name: name of the user seeking a new friend.
        :return: None.
        """
        pass

    def display_number_of_friends(self, data: SocialNetwork, user_name: str):
        """
        Prints the number of friends for a given user.
        :param data: list of users and their friends.
        :param user_name: name of the user to output its number of friends.
        :return: None.
        """
        pass

    def display_least_num_friends(self, data: SocialNetwork):
        """
        Prints the names of the user s with less than 2 friends.
        :param data: list of users and their friends.
        :return: None.
        """
        pass

    def display_user_relationship(self, data: SocialNetwork, user_name: str):
        """
        Prints the username and their list of friends.
        :param data: list of users and their friends.
        :param user_name: name of the user to output.
        :return: None.
        """
        pass

    def display_indirect_relationships(self, data: SocialNetwork):
        """
        Prints indirect relations of users.
        :param data: list of users and their friends.
        :return: None.
        """
        pass
