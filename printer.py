from social_network import SocialNetwork
from user import User


class Printer:
    """
    Displays the social network on the Python console.
    """
    @staticmethod
    def display_network(data: SocialNetwork):
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

    @staticmethod
    def display_common_friends(data: SocialNetwork):
        """
        Pretty prints the number of common friends per pair of users.
        :param data: list of users and number of common friends with each of the other users to output.
        :return: None.
        """
        all_common_friends: dict[(str, str), int] = data.common_friends
        common_friends_matrix: dict[str, list[int]] = data.generate_common_friends(all_common_friends)
        for user_name in common_friends_matrix:
            print(f"{user_name} -> {common_friends_matrix[user_name]}")

    @staticmethod
    def display_recommended_friend(data: SocialNetwork, user_name: str):
        """
        Prints the friend recommendation for a given user.
        :param data: list of users and their friends.
        :param user_name: name of the user seeking a new friend
        :return: None.
        """
        recommended = data.recommend_friend(user_name)
        print(f"The recommended friend for {user_name} is {recommended}")
