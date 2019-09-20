from item import Item


class Journal(Item):
    def __init__(self, title, call_number, author, num_copies, issue_number, publisher):
        self.author = author
        self.issue_number = issue_number
        self.publisher = publisher
        super().__init__(title, call_number, num_copies)

    def __str__(self):
        return f'Item type: Journal; {super().__str__()}; author: {self.author};' \
               f' issue_number: {self.issue_number}; publisher: {self.publisher}'

