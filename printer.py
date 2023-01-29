from social_network import SocialNetwork


class Printer:
    """
    Displays the social network.
    """
    # Feature 1 ii.
    def display_network(self, data: SocialNetwork):
        """
        Prints the social network.
        :param data: list of users and their friends to output.
        :return: None.
        """
        pass

    # Feature 2 i.
    def display_common_friends(self, data: SocialNetwork):
        """
        Prints the number of common friends per pair of users.
        :param data: list of users and number of common friends with each of the other users to output.
        :return: None.
        """
        pass

    # Feature 2 ii.
    def display_recommended_friend(self, data: SocialNetwork, user_name: str):
        """
        Prints the friend recommendation for a given user.
        :param data: list of users and their friends.
        :param user_name: name of the user seeking a new friend.
        :return: None.
        """
        pass

    # Feature 3 i.
    def display_number_of_friends(self, data: SocialNetwork, user_name: str):
        """
        Prints the number of friends for a given user.
        :param data: list of users and their friends.
        :param user_name: name of the user to output its number of friends.
        :return: None.
        """
        pass

    # Feature 3 ii.
    def display_least_num_friends(self, data: SocialNetwork):
        """
        Prints the names of the user s with less than 2 friends.
        :param data: list of users and their friends.
        :return: None.
        """
        pass

    # Feature 3 iii.
    def display_user_relationship(self, data: SocialNetwork, user_name: str):
        """
        Prints the username and their list of friends.
        :param data: list of users and their friends.
        :param user_name: name of the user to output.
        :return: None.
        """
        pass

    # Feature 3 iv.
    def display_indirect_relationships(self, data: SocialNetwork):
        """
        Prints indirect relations of users.
        :param data: list of users and their friends.
        :return: None.
        """
        pass
