from abc import ABC


class Card(ABC):
    def __init__(self, card_name, card_holder, issued_by):
        self.card_name = card_name
        self.card_holder = card_holder
        self.issued_by = issued_by

    def get_card_name(self):
        return self.card_name

    def set_card_name(self):
        return self.card_name

    def __str__(self):
        return f'{self.card_name}'
