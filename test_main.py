from unittest import TestCase
from user import User


class TestUser(TestCase):
    def test_init(self):
        user: User = User("Sebi")
        self.assertEqual('Sebi', user.name, "Wrong user name!")
        self.assertListEqual([], user.friend_names, "Wrong list of friends!")

    def test_add_friend(self):
        user: User = User("Sebi")
        user.add_friend("Vlad")
        self.assertIn("Vlad", user.friend_names, "Wrong friend!")
