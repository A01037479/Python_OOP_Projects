from abc import ABC


class Card(ABC):
    def __init__(self, card_name, card_holder, issued_by):
        self.card_name = card_name
        self.card_holder = card_holder
        self.issued_by = issued_by

    def get_card_name(self):
        return self.card_name

    def __str__(self):
        return f'Card name: {self.card_name}; Card holder: {self.card_holder};' \
               f' Issued by: {self.issued_by}'


class Expirable(ABC):
    def __init__(self, issue_date, expiry_date):
        self.issue_date = issue_date
        self.expiry_date = expiry_date

    def __str__(self):
        return f' Issue date: {self.issue_date};' \
               f' Expiry date: {self.expiry_date}'


class Other(Card):
    def __init__(self, card_name, card_holder, issued_by, card_description):
        super().__init__(card_name, card_holder, issued_by)
        self.description = card_description

    def __str__(self):
        return super().__str__() + f'; Description: {self.description}'


class RewardCard(Card):
    def __init__(self, card_name, card_holder, issued_by, reward_type):
        super().__init__(card_name, card_holder, issued_by)
        self.reward_type = reward_type

    def __str__(self):
        return super().__str__() + f'; Reward type: {self.reward_type}'


class BalanceCard(Card):
    def __init__(self, card_name, card_holder, issued_by, balance):
        super().__init__(card_name, card_holder, issued_by)
        self.balance = balance

    def __str__(self):
        return super().__str__() + f'; Balance: {self.balance}'


class MembershipCard(Card, Expirable):
    def __init__(self, card_name, card_holder, issued_by, issue_date,
                 expiry_date, membership_level):
        Card.__init__(self, card_name, card_holder, issued_by)
        Expirable.__init__(self, issue_date, expiry_date)
        self.membership_level = membership_level

    def __str__(self):
        return Card.__str__(self) + Expirable.__str__(self) + \
               f'; Membership level: {self.membership_level}'


class BankCard(Card, Expirable):
    def __init__(self, card_name, card_holder, issued_by, issue_date,
                 expiry_date, bank_info):
        Card.__init__(self, card_name, card_holder, issued_by)
        Expirable.__init__(self, issue_date, expiry_date)
        self.bank_info = bank_info

    def __str__(self):
        return Card.__str__(self) + Expirable.__str__(self) + \
               f'; Bank information: {self.bank_info}'


class IDCard(Card, Expirable):
    def __init__(self, card_name, card_holder, issued_by, issue_date,
                 expiry_date, id_number):
        Card.__init__(self, card_name, card_holder, issued_by)
        Expirable.__init__(self, issue_date, expiry_date)
        self.id_number = id_number

    def __str__(self):
        return Card.__str__(self) + Expirable.__str__(self) + \
               f'; ID number: {self.id_number}'


class GovIDCard(IDCard):
    def __init__(self, card_name, card_holder, issued_by, issue_date,
                 expiry_date, id_number, personal_information):
        IDCard.__init__(self, card_name, card_holder, issued_by,
                        issue_date, expiry_date, id_number)
        self.personal_information = personal_information

    def __str__(self):
        return super().__str__() + f'; Age: {self.personal_information["age"]}' \
                                   f'; Sex: {self.personal_information["sex"]}' \
                                   f'; Height: {self.personal_information["height"]}cm'
