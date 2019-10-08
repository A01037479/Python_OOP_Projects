from card import Card


class LoyaltyCard(Card):
    def __init__(self, card_name, card_holder, issued_by, reward):
        super().__init__(card_name, card_holder, issued_by)
        self.reward = reward
