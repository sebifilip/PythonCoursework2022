from typing import Optional
from user import User


class SocialNetwork:
    """
    Encapsulation of the users and their friends.
    """
    users: dict[str, User]
    common_friends: dict[(str, str), int]

    def __init__(self):
        """
        Initialises the map of users to empty.
        """
        self.users = {}
        self.common_friends = None

    def add_user(self, user_name: str) -> User:
        """
        Adds a user to the network if it does not exist.
        :param user_name: name of the user to add.
        :return: user object corresponding to the given name.
        """
        if user_name not in self.users:
            self.users[user_name] = User(user_name)
        return self.users[user_name]

    def add_friend(self, user_name: str, friend_name: str) -> User:
        """
        Associates a user to a new friend.
        :param user_name: name of user to associate.
        :param friend_name: name of friend to associate with.
        :return: user object corresponding to the friend.
        """
        user: User = self.add_user(user_name)
        friend: User = self.add_user(friend_name)
        user.add_friend(friend_name)
        friend.add_friend(user_name)
        return friend

    def get_user(self, user_name: str) -> Optional[User]:
        """
        Gets the user associated with given name, if any.
        :param user_name: name of user to get.
        :return: user object corresponding to the name or None.
        """
        if user_name in self.users:
            return self.users[user_name]
        return None

    def get_friends(self, user_name: str) -> list[User]:
        """
        Gets the list of objects corresponding to the friends of the given user.
        :param user_name: name of user to get friends of, if any.
        :return: list of friend objects or empty list if user does not exist.
        """
        user: User = self.get_user(user_name)
        if user is None:
            return []
        result: list[User] = []
        for friend_name in user.friend_names:
            friend: User = self.get_user(friend_name)
            result += [friend]
        return result

    def generate_common_friends(self, common_friends: dict[(str, str), int]) -> dict[str, list[int]]:
        """
        Generates a matrix containing the number of common friends for every pair of users in the social network.
        :param common_friends: dictionary containing a pair of users as the keys and the number of common friends as
        the values.
        :return: dictionary containing each username as keys and lists of common friends associated with
        the other users as the values.
        """
        common_matrix = {}
        for name in sorted(self.users.keys()):
            common_matrix[name] = []
        for user in common_matrix:
            ln: dict[str, int] = {}
            for (n1, n2) in common_friends:
                if user == n1:
                    ln[n2] = common_friends[(n1, n2)]
            u = self.users[user]
            ln[user] = len(u.friend_names)
            for n2 in sorted(ln.keys()):
                common_matrix[user] += [ln[n2]]
        return common_matrix

    def get_common_friends(self) -> dict[(str, str), int]:
        """
        Gets the number of common friends for each pair of friends in the social network.
        :return: dictionary containing number of common friends for each pair.
        """
        if self.common_friends is None:
            self.common_friends = self._compute_common_friends()
        return self.common_friends

    def _compute_common_friends(self) -> dict[(str, str), int]:
        result: dict[(str, str), int] = {}
        for name1 in self.users.keys():
            for name2 in self.users.keys():
                if name1 != name2:
                    result[(name1, name2)] = self._compute_friends_count(name1, name2)
        return result

    def _compute_friends_count(self, name1: str, name2: str) -> int:
        l1 = self.users[name1].friend_names
        l2 = self.users[name2].friend_names
        common_num = 0
        for n in l1:
            if n == name1 or n == name2:
                continue
            if n in l2:
                common_num += 1
        return common_num

    def recommend_friend(self, user_name: str) -> Optional[str]:
        """
        Gets a username as a parameter and recommends a new friend based on the number of common friends with that
        potential friend.
        :param user_name: name of a user seeking a new friend.
        :return: recommended friend or None.
        """
        u: User = self.users[user_name]
        if not u.friend_names:
            return None
        cf = self.get_common_friends()
        max_common = 0
        result = None
        for (n1, n2) in cf.keys():
            if n1 == user_name:
                if n2 in u.friend_names:
                    continue
                if cf[(n1, n2)] > max_common:
                    max_common = cf[(n1, n2)]
                    result = n2
        return result