from social_network import SocialNetwork
from user import User
from printer import Printer


class ConsolePrinter(Printer):
    """
    Displays the social network on the Python console.
    """
    def display_network(self, data: SocialNetwork):
        """
        Pretty prints the social network on the Python terminal.
        :param data: list of users and their friends to output.
        :return: None.
        """
        all_users: dict[str, User] = data.users
        for user_name in sorted(all_users.keys()):
            user_friends: list[User] = data.get_friends(user_name)
            friend_names: list[str] = []
            for friend in user_friends:
                friend_names += [friend.name]
            friend_names_str: str = ", ".join(sorted(friend_names))
            print(f"{user_name} -> {friend_names_str}")

    def display_common_friends(self, data: SocialNetwork):
        """
        Pretty prints the number of common friends per pair of users.
        :param data: list of users and number of common friends with each of the other users to output.
        :return: None.
        """
        all_common_friends: dict[(str, str), int] = data.common_friends
        common_friends_matrix: dict[str, list[int]] = data.generate_common_friends(all_common_friends)
        for user_name in common_friends_matrix:
            print(f"{user_name} -> {common_friends_matrix[user_name]}")

    def display_recommended_friend(self, data: SocialNetwork, user_name: str):
        """
        Prints the friend recommendation for a given user.
        :param data: list of users and their friends.
        :param user_name: name of the user seeking a new friend.
        :return: None.
        """
        recommended: str = data.recommend_friend(user_name)
        print(f"The recommended friend for {user_name} is {recommended}")

    def display_number_of_friends(self, data: SocialNetwork, user_name: str):
        """
        Prints the number of friends for a given user.
        :param data: list of users and their friends.
        :param user_name: name of the user to output its number of friends.
        :return:
        """
        u: User = data.users[user_name]
        print(f"{user_name} has {len(u.friend_names)} friends")

    def display_least_num_friends(self, data: SocialNetwork):
        """
        Prints the names of the user s with less than 2 friends.
        :param data: list of users and their friends.
        :return: None.
        """
        zero_friends: list[str] = []
        one_friend: list[str] = []
        for name in sorted(data.users.keys()):
            user: User = data.users[name]
            if len(user.friend_names) == 1:
                one_friend.append(name)
            elif len(user.friend_names) == 0:
                zero_friends.append(name)
        str_zero: str = ", ".join(sorted(zero_friends))
        str_one: str = ", ".join(sorted(one_friend))
        print(f"The user name with least friends is: {str_one}")
        print(f"The user name with zero friends is: {str_zero}")

    def display_user_relationship(self, data: SocialNetwork, user_name: str):
        """
        Prints the username and their list of friends.
        :param data: list of users and their friends.
        :param user_name: name of the user to output.
        :return: None.
        """
        relationship = data.get_user_relationship(user_name)
        str_relationship: str = ", ".join(sorted(relationship[user_name]))
        print(f"{user_name} is friends with {str_relationship}")

    def display_indirect_relationships(self, data: SocialNetwork):
        """
        Prints indirect relations of users.
        :param data: list of users and their friends.
        :return: None.
        """
        indirect = data.get_indirect_relationships()
        for user_name in indirect:
            if len(indirect[user_name]) > 0:
                str_indirect = ", ".join(sorted(indirect[user_name]))
                print(f"{user_name} -> {str_indirect}")
