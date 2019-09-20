from item import Item


class Book(Item):
    def __init__(self, title, call_number, author, num_copies):
        self.author = author
        super().__init__(title, call_number, num_copies)

    def __str__(self):
        return f'Item type: book; author: {self.author}; {super().__str__()}'
