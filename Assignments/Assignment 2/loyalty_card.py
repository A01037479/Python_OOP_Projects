from card import Card


class LoyaltyCard(Card):
    def __init__(self, reward):
        super().__init__()
        self.reward = reward