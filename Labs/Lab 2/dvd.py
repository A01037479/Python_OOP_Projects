from item import Item


class DVD(Item):
    def __init__(self, title, call_number, num_copies, release_date, region_code):
        self.release_date = release_date
        self.region_code = region_code
        super().__init__(title, call_number, num_copies)

    def __str__(self):
        return f'Item type: DVD; {super().__str__()}; release_date: {self.release_date}; region_code: {self.region_code} '

