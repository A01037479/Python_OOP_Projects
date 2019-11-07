from item import Item


class Book(Item):
    """
    A book class that inherents from Item class
    """
    def __init__(self, title, call_number, author, num_copies):
        """
        Initialize an book
        :param title: String
        :param call_number: String
        :param author: String
        :param num_copies: Int
        """
        self.author = author
        super().__init__(title, call_number, num_copies)

    def __str__(self):
        """
        String representation of a book
        :return: String
        """
        return f'Item type: book; author: {self.author}; {super().__str__()}'
