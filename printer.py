from social_network import SocialNetwork
from user import User


class Printer:
    """
    Displays the social network.
    """
    def display_network(self, data: SocialNetwork):
        pass

    def display_common_friends(self, data: SocialNetwork):
        pass

    def display_recommended_friend(self, data: SocialNetwork, user_name: str):
        pass

    def display_number_of_friends(self, data: SocialNetwork, user_name: str):
        pass

    def display_least_num_friends(self, data: SocialNetwork):
        pass

    def display_user_relationship(self, data: SocialNetwork, user_name: str):
        pass

    def display_indirect_relationships(self, data: SocialNetwork):
        pass
