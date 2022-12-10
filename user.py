class User:
    """
    Encapsulation of a user with the names of its friends.
    """
    name: str
    friend_names: list[str]

    def __init__(self, user_name: str):
        """
        Initialises the user object with an empty list of friend names.
        :param user_name: name of the user.
        """
        self.name = user_name
        self.friend_names = []

    def add_friend(self, friend_name: str):
        """
        Adds a name to the list of friend names.
        :param friend_name: name of the friend to add.
        :return: None
        """
        self.friend_names += [friend_name]
