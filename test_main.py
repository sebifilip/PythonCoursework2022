from unittest import TestCase
from user import User
from social_network import SocialNetwork


class TestUser(TestCase):
    def test_init(self):
        user: User = User("Sebi")
        self.assertEqual('Sebi', user.name, "Wrong user name!")
        self.assertListEqual([], user.friend_names, "Wrong list of friends!")

    def test_add_friend(self):
        user: User = User("Sebi")
        user.add_friend("Vlad")
        self.assertIn("Vlad", user.friend_names, "Wrong friend!")


class TestSocialNetwork(TestCase):
    def test_init(self):
        network: SocialNetwork = SocialNetwork()
        self.assertDictEqual({}, network.users, "Social network not empty.")

    def test_add_user(self):
        network: SocialNetwork = SocialNetwork()
        user: User = network.add_user("Sebi")
        self.assertEqual("Sebi", user.name, "Wrong user name!")

    def test_add_same_user(self):
        network: SocialNetwork = SocialNetwork()
        user: User = network.add_user("Sebi")
        other_user: User = network.add_user("Sebi")
        self.assertIs(user, other_user, "Different objects!")

    def test_add_different_user(self):
        network: SocialNetwork = SocialNetwork()
        user: User = network.add_user("Sebi")
        other_user: User = network.add_user("Dinu")
        other_user.name = "Sebi"
        self.assertIsNot(user, other_user, "Same object!")

    def test_add_friend(self):
        network: SocialNetwork = SocialNetwork()
        friend: User = network.add_friend("Sebi", "Emil")
        self.assertEqual("Emil", friend.name, "Wrong friend name!")
        self.assertIn("Sebi", friend.friend_names, "Missing friend!")

    def test_get_user(self):
        network: SocialNetwork = SocialNetwork()
        added_user: User = network.add_user("Sebi")
        gotten_user: User = network.get_user("Sebi")
        self.assertIs(added_user, gotten_user, "Different users!")

    def test_get_users_friend(self):
        network: SocialNetwork = SocialNetwork()
        friend: User = network.add_friend("Sebi", "Emil")
        user: User = network.get_user("Sebi")
        self.assertIn(friend.name, user.friend_names, "Missing friend!")

    def test_get_friends(self):
        network: SocialNetwork = SocialNetwork()
        for friend in ["Emil", "Dinu", "Vlad"]:
            network.add_friend("Sebi", friend)
        friends: list[User] = network.get_friends("Sebi")
        friend_names: list[str] = []
        for friend in friends:
            friend_names += [friend.name]
        for name in ["Emil", "Dinu", "Vlad"]:
            self.assertIn(name, friend_names, "Friend not in list!")

