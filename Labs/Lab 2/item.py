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
        self.title = title
        self.call_number = call_number
        self.num_copies = num_copies

    def get_title(self):
        """
        Accessor of item title
        :return: String
        """
        return self.title

    def get_call_number(self):
        """
        Accessor of item call number
        :return: String
        """
        return self.call_number

    def get_num_copies(self):
        """
        Accessor of item number of copies
        :return: int
        """
        return self.num_copies

    def set_num_copies(self, num_copies):
        """
        Mutator of item number of copies
        :param num_copies: int
        :return: int
        """
        self.num_copies = num_copies

    def check_availability(self):
        """
        Checks if an item is available
        :return: True if item available, False otherwise
        """
        if int(self.num_copies) >= 1:
            return True
        else:
            return False

    def __str__(self):
        """
        String representation of an item
        :return: String
        """
        return (f' title: {self.title}; call number: {self.call_number};'
                f' number of copy: {self.num_copies}')
