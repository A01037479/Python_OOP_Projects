from book import Book


class Library:
    def __init__(self, book_list):
        self.book_list = book_list

    def add_book(self, book):
        if book not in self.book_list:
            self.book_list.append(book)

    def remove_book(self, call_number):
        i = 0
        while i < self.book_list.length:
            if self.book_list[i].call_number == call_number:
                self.book_list.remove(self.book_list[i])
                return True
            i += 1
        return False

    def check_out(self, call_number):
        i = 0
        while i < self.book_list.length:
            if self.book_list[i].call_number == call_number:
                self.book_list.num_copies -= 1
                return True
            i += 1
        return False

    def return_book(self, call_number):
        i = 0
        while i < self.book_list.length:
            if self.book_list[i].call_number == call_number:
                self.book_list.num_copies += 1
                return True
            i += 1
        return False

    def display_available_books(self):
        i = 0
        print('Available books:')
        while i < self.book_list.length:
            print(self.book_list[i])
            i += 1

    def find_books(self, title):
        i = 0
        while i < self.book_list.length:
            if self.book_list[i].title == title:
                return self.book_list[i]
            i += 1
