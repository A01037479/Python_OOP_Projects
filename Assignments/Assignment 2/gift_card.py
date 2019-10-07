from card import Card


class GiftCard(Card):
    def __init__(self):
        super().__init__()
        self.gift_value = None
