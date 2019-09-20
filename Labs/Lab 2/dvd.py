from item import Item


class DVD(Item):
    """
    A DVD class that inherents from Item class
    """
    def __init__(self, title, call_number, num_copies, release_date, region_code):
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
        return f'Item type: DVD; {super().__str__()}; release_date: {self.release_date}; region_code: {self.region_code} '

