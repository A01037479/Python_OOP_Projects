import abc


class Item(abc.ABC):
    """
    A class that represents an item
    """

    def __init__(self, title, call_number, num_copies):
        """
        initializes an item object
        :param title: String
        :param call_number: String
        :param num_copies: Int
        """
        self._title = title
        self._call_number = call_number
        self._num_copies = num_copies

    def get_title(self):
        """
        Accessor of item title
        :return: String
        """
        return self._title

    def get_call_number(self):
        """
        Accessor of item call number
        :return: String
        """
        return self._call_number

    def set_call_number(self, value):
        self._call_number = value

    call_number = property(get_call_number, set_call_number)

    def get_num_copies(self):
        """
        Accessor of item number of copies
        :return: int
        """
        return self._num_copies

    def set_num_copies(self, num_copies):
        """
        Mutator of item number of copies
        :param num_copies: int
        :return: int
        """
        self._num_copies = num_copies

    num_copies = property(get_num_copies, set_num_copies)

    def check_availability(self):
        """
        Checks if an item is available
        :return: True if item available, False otherwise
        """
        if int(self._num_copies) >= 1:
            return True
        else:
            return False

    def __str__(self):
        """
        String representation of an item
        :return: String
        """
        return (f' title: {self._title}; call number: {self._call_number};'
                f' number of copy: {self._num_copies}')


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


class DVD(Item):
    """
    A DVD class that inherents from Item class
    """

    def __init__(self, title, call_number, num_copies, release_date,
                 region_code):
        """
        Initializes a DVD
        :param title: String
        :param call_number: String
        :param num_copies: Int
        :param release_date: String
        :param region_code: String
        """
        self.release_date = release_date
        self.region_code = region_code
        super().__init__(title, call_number, num_copies)

    def __str__(self):
        """
        String representation of a DVD
        :return: String
        """
        return f'Item type: DVD; {super().__str__()}; release_date: ' \
               f'{self.release_date}; region_code: {self.region_code} '


class Journal(Item):
    """
    A Journal class that inherents from Item class
    """

    def __init__(self, title, call_number, author, num_copies, issue_number,
                 publisher):
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
        return f'Item type: Journal; {super().__str__()}; author: ' \
               f'{self.author}; issue_number: {self.issue_number}; ' \
               f'publisher: {self.publisher}'
