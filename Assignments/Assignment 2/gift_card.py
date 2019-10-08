from card import Card


class GiftCard(Card):
    def __init__(self, card_name, card_holder, issued_by, gift_value):
        super().__init__(card_name, card_holder, issued_by)
        self.gift_value = gift_value
