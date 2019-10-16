"""
The module contains CardManager class which deals with actions on cards.
"""
from file_handler import FileHandler
from card import Card, Expirable, Other, RewardCard, BalanceCard, \
    MembershipCard, BankCard, IDCard, GovIDCard


class CardManager:
    """
    CardManager class encapsulates all methods that use cards.
    """
    card_type_dict = {1: RewardCard, 2: BalanceCard, 3: MembershipCard,
                      4: BankCard, 5: IDCard, 6: GovIDCard,
                      7: Other}
    card_str_type_dict = {1: 'Reward Card', 2: 'Balance Card',
                          3: 'Membership Card',
                          4: 'Bank Card', 5: 'ID Card',
                          6: 'Government ID Card', 7: 'Other'}

    def __init__(self):
        self.cards = []

    def card_name(self, card):
        """
        Takes in a Card and returns its name.
        :param card: Card
        :return: Card
        """
        return card.get_card_name()

    def add_card(self, card):
        """
        Appends a Card into Cards dictionary.
        :param card: Card
        """
        self.cards.append(card)

    def remove_card(self, card):
        """
        Removes a Card from Cards dictionary.
        :param card: Card
        """
        self.cards.remove(card)

    def view_all_cards(self):
        """
        Prints all Card objects from Cards dictionary.
        """
        for card in self.cards:
            print(card)

    def view_card_by_type(self, card_type):
        """
        Prints all Card objects that are specified type from Cards dictionary.
        :param card_type: int
        """
        found = False
        for card in self.cards:
            if card.__class__ == self.card_type_dict[card_type]:
                found = True
                print(card)
        if not found:
            print(f'There is no {self.card_str_type_dict[card_type]} '
                  f'currently in the card manager')

    def search_card(self, card):
        """
        Searches a card object from Cards dictionary.
        """
        if card in self.cards:
            print(card)

    def back_up_data(self, path):
        """
        Prints all Card objects into a file in path.
        :param path: String
        """
        for card in self.cards:
            FileHandler.write_line(path, str(card))

    @staticmethod
    def create_other(card_name, card_holder, issued_by, card_description):
        return Other(card_name, card_holder, issued_by, card_description)

    @staticmethod
    def create_reward_card(card_name, card_holder, issued_by, reward_type):
        return RewardCard(card_name, card_holder, issued_by, reward_type)

    @staticmethod
    def create_balance_card(card_name, card_holder, issued_by, balance):
        return BalanceCard(card_name, card_holder, issued_by, balance)

    @staticmethod
    def create_membership_card(card_name, card_holder, issued_by, issue_date,
                               expiry_date, membership_level):
        return MembershipCard(card_name, card_holder, issued_by, issue_date,
                              expiry_date, membership_level)

    @staticmethod
    def create_bank_card(card_name, card_holder, issued_by, issue_date,
                         expiry_date, bank_info):
        return BankCard(card_name, card_holder, issued_by, issue_date,
                        expiry_date, bank_info)

    @staticmethod
    def create_id_card(card_name, card_holder, issued_by, issue_date,
                       expiry_date, id_number):
        return IDCard(card_name, card_holder, issued_by, issue_date,
                      expiry_date, id_number)

    @staticmethod
    def create_gov_id_card(card_name, card_holder, issued_by, issue_date,
                           expiry_date, id_number, personal_information):
        return GovIDCard(card_name, card_holder, issued_by, issue_date,
                         expiry_date, id_number, personal_information)
