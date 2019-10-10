from abc import ABC


class Card(ABC):
    def __init__(self, card_name, card_holder, issued_by):
        self.card_name = card_name
        self.card_holder = card_holder
        self.issued_by = issued_by

    def __str__(self):
        return f'{self.card_name}'

class Expirable(ABC):
    def __init__(self, issue_date, expiry_date):
        self.issue_date = issue_date
        self.expiry_date = expiry_date


class Other(Card):
    def __init__(self, card_name, card_holder, issued_by, card_description):
        super().__init__(card_name, card_holder, issued_by)
        self.self_description = card_description


class RewardCard(Card):
    def __init__(self, card_name, card_holder, issued_by, reward_type):
        super().__init__(card_name, card_holder, issued_by)
        self.reward_type = reward_type


class BalanceCard(Card):
    def __init__(self, card_name, card_holder, issued_by, balance):
        super().__init__(card_name, card_holder, issued_by)
        self.balance = balance


class MembershipCard(Card, Expirable):
    def __init__(self, card_name, card_holder, issued_by, issue_date,
                 expiry_date, membership_level):
        Card.__init__(self, card_name, card_holder, issued_by)
        Expirable.__init__(self, issue_date, expiry_date)
        self.membership_level = membership_level


class BankCard(Card, Expirable):
    def __init__(self, card_name, card_holder, issued_by, issue_date,
                 expiry_date, bank_info):
        Card.__init__(self, card_name, card_holder, issued_by)
        Expirable.__init__(self, issue_date, expiry_date)
        self.bank_info = bank_info


class IDCard(Card, Expirable):
    def __init__(self, card_name, card_holder, issued_by, issue_date,
                 expiry_date, id_number):
        Card.__init__(self, card_name, card_holder, issued_by)
        Expirable.__init__(self, issue_date, expiry_date)
        self.id_number = id_number


class GovIDCard(IDCard):
    def __init__(self, card_name, card_holder, issued_by, issue_date,
                 expiry_date, id_number, personal_information):
        IDCard.__init__(self, card_name, card_holder, issued_by,
                        issue_date, expiry_date, id_number)
        self.personal_information = personal_information
