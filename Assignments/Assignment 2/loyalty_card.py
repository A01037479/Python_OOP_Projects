from card import Card


class LoyaltyCard(Card):
    def __init__(self):
        super().__init__()
        self.reward = None