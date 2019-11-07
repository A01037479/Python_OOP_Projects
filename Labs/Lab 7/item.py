class Item:
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
