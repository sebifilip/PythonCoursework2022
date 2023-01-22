from unittest import TestCase
from user import User
from social_network import SocialNetwork


class TestUser(TestCase):
    def test_init(self):
        user: User = User("Adam")
        self.assertEqual('Adam', user.name, "Wrong user name!")
        self.assertListEqual([], user.friend_names, "Wrong list of friends!")

    def test_add_friend(self):
        user: User = User("Adam")
        user.add_friend("Amir")
        self.assertIn("Amir", user.friend_names, "Wrong friend!")


class TestSocialNetwork(TestCase):
    def test_init(self):
        network: SocialNetwork = SocialNetwork()
        self.assertDictEqual({}, network.users, "Social network not empty.")

    def test_add_user(self):
        network: SocialNetwork = SocialNetwork()
        user: User = network.add_user("Adam")
        self.assertEqual("Adam", user.name, "Wrong user name!")

    def test_add_same_user(self):
        network: SocialNetwork = SocialNetwork()
        user: User = network.add_user("Adam")
        other_user: User = network.add_user("Adam")
        self.assertIs(user, other_user, "Different objects!")

    def test_add_different_user(self):
        network: SocialNetwork = SocialNetwork()
        user: User = network.add_user("Adam")
        other_user: User = network.add_user("Bob")
        other_user.name = "Adam"
        self.assertIsNot(user, other_user, "Same object!")

    def test_add_friend(self):
        network: SocialNetwork = SocialNetwork()
        friend: User = network.add_friend("Adam", "Chris")
        self.assertEqual("Chris", friend.name, "Wrong friend name!")
        self.assertIn("Adam", friend.friend_names, "Missing friend!")

    def test_get_user(self):
        network: SocialNetwork = SocialNetwork()
        added_user: User = network.add_user("Adam")
        gotten_user: User = network.get_user("Adam")
        self.assertIs(added_user, gotten_user, "Different users!")

    def test_get_users_friend(self):
        network: SocialNetwork = SocialNetwork()
        friend: User = network.add_friend("Adam", "Chris")
        user: User = network.get_user("Adam")
        self.assertIn(friend.name, user.friend_names, "Missing friend!")

    def test_get_friends(self):
        network: SocialNetwork = SocialNetwork()
        for friend in ["Chris", "Bob", "Amir"]:
            network.add_friend("Adam", friend)
        friends: list[User] = network.get_friends("Adam")
        friend_names: list[str] = []
        for friend in friends:
            friend_names += [friend.name]
        for name in ["Chris", "Bob", "Amir"]:
            self.assertIn(name, friend_names, "Friend not in list!")
