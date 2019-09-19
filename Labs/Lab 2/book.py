class Book:
    def __init__(self, title, call_number, author, num_copies):
        self.title = title
        self.call_number = call_number
        self.author = author
        self.num_copies = num_copies

    def get_title(self):
        return self.title

    def get_call_number(self):
        return self.call_number

    def get_author(self):
        return self.author

    def get_num_copies(self):
        return self.num_copies

    def set_num_copies(self, num_copies):
        self.num_copies = num_copies

    def check_availability(self):
        if self.num_copies >= 1:
            return True
        else:
            return False

    def __str__(self):
        return (f'Book title: {self.title}; call number: {self.call_number};'
                f' author: {self.author}; number of copy: {self.num_copies}')
