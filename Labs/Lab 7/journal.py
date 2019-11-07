from item import Item


class Journal(Item):
    """
    A Journal class that inherents from Item class
    """
    def __init__(self, title, call_number, author, num_copies, issue_number, publisher):
        """
        Initializes a journal
        :param title: String
        :param call_number:String
        :param author:String
        :param num_copies:Int
        :param issue_number:String
        :param publisher:String
        """
        self.author = author
        self.issue_number = issue_number
        self.publisher = publisher
        super().__init__(title, call_number, num_copies)

    def __str__(self):
        """
        String representation of a journal
        :return: String
        """
        return f'Item type: Journal; {super().__str__()}; author: {self.author};' \
               f' issue_number: {self.issue_number}; publisher: {self.publisher}'

