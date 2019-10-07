class Card:
    def __init__(self):
        self.card_name = None
        self.card_holder = None
        self.issued_by = None

    def get_card_name(self):
        return self.card_name

    def set_card_name(self):
        return self.card_name

    def __str__(self):
        return f'{self.card_name}'
