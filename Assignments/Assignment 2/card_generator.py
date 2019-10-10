from card import Card, Expirable, Other, RewardCard, BalanceCard, \
    MembershipCard, BankCard, IDCard, GovIDCard


class CardGenerator:
    card_type_dict = {'1': RewardCard, '2': BalanceCard, '3': MembershipCard,
                      '4': BankCard, '5': IDCard, '6': GovIDCard,
                      '7': Other}
    card_str_type_dict = {'1': 'Reward Card', '2': 'Balance Card',
                          '3': 'Membership Card',
                          '4': 'Bank Card', '5': 'ID Card',
                          '6': 'Government ID Card', '7': 'Other'}
    card_types = card_type_dict.values()

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
