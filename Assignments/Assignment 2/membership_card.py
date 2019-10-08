from card import Card


class MembershipCard(Card):
    def __init__(self, card_name, card_holder, issued_by, membership_level):
        super().__init__(card_name, card_holder, issued_by)
        self.membership_level = membership_level
