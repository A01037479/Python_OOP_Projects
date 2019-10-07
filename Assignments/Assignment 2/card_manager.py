from file_handler import FileHandler


class CardManager:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def view_card_by_type(self, card_type):
        for card in self.cards:
            if card.__class__.__name__ == card_type:
                print(card)

    def search_card(self, card):
        if card in self.cards:
            print(card)
        else:
            print('Card not found')

    def back_up_data(self, path):
        for card in self.cards:
            try:
                FileHandler.writeline(path, card.str())
            except TypeError as e:
                print(f'InvalidFileTypeError caught! {e}')