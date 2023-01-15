from social_network import SocialNetwork
from printer import Printer
from typing import Optional


class PrintableSocialNetwork(SocialNetwork):

    _printer: Printer

    def __init__(self, printer: Printer, data: Optional[SocialNetwork] = None):
        SocialNetwork.__init__(self)
        self._printer = printer
        self._data = self if data is None else data

    def display_network(self):
        self._printer.display_network(self._data)

    def display_common_friends(self):
        self._printer.display_common_friends(self._data)

    def display_recommended_friend(self, user_name: str):
        self._printer.display_recommended_friend(self._data, user_name)

    def display_number_of_friends(self, user_name: str):
        self._printer.display_number_of_friends(self._data, user_name)

    def display_least_num_friends(self):
        self._printer.display_least_num_friends(self._data)

    def display_user_relationship(self, user_name: str):
        self._printer.display_user_relationship(self._data, user_name)

    def display_indirect_relationships(self):
        self._printer.display_indirect_relationships(self._data)
