from card import Card


class MembershipCard(Card):
    def __init__(self):
        super().__init__()
        self.membership_level = None
