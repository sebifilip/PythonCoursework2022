from social_network import SocialNetwork
from printer import Printer


class PrintableSocialNetwork(SocialNetwork):

    _printer: Printer

    def __init__(self, printer: Printer):
        SocialNetwork.__init__(self)
        self._printer = printer

    def display_network(self):
        self._printer.display_network(self)

    def display_common_friends(self):
        self._printer.display_common_friends(self)

    def display_recommended_friend(self, user_name: str):
        self._printer.display_recommended_friend(self, user_name)

    def display_number_of_friends(self, user_name: str):
        self._printer.display_number_of_friends(self, user_name)

    def display_least_num_friends(self):
        self._printer.display_least_num_friends(self)

    def display_user_relationship(self, user_name: str):
        self._printer.display_user_relationship(self, user_name)

    def display_indirect_relationships(self):
        self._printer.display_indirect_relationships(self)
