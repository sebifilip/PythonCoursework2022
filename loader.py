from social_network import SocialNetwork


# Feature 1 ii.
class Loader:
    """
    Opens and reads a .txt file of social network of users.
    """
    def load_network(self, location: str) -> SocialNetwork:
        """
        Opens the data file, reads the users and returns the social network.
        :param location: where to get data from. Here, it is the name of the data file to open and read.
        :return: social network object.
        """
        sn: SocialNetwork = SocialNetwork()
        i = 0
        with open(location, "r") as reader:
            for line in reader.readlines():
                line = line.strip()
                if i > 0:
                    connection: list[str] = line.split()
                    if len(connection) == 1:
                        user_name: str = connection[0]
                        sn.add_user(user_name)
                    elif len(connection) == 2:
                        user_name, friend_name = connection
                        sn.add_friend(user_name, friend_name)
                    else:
                        raise ValueError("Social network line does not have one or two elements: " + line)
                i += 1
        sn.validate()
        return sn
