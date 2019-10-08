from card import Card


class DebitCard(Card):
    def __init__(self, card_name, card_holder, issued_by):
        super().__init__(card_name, card_holder, issued_by)
