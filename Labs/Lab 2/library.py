import keyword
from difflib import get_close_matches

from book import Book


class Library:
    def __init__(self, book_list):
        self.book_list = book_list

    def add_book(self, book):
        if book not in self.book_list:
            self.book_list.append(book)

    def remove_book(self, call_number):
        i = 0
        while i < len(self.book_list):
            if self.book_list[i].get_call_number() == call_number:
                self.book_list.remove(self.book_list[i])
                return True
            i += 1
        return False

    def check_out(self, call_number):
        i = 0
        while i < len(self.book_list):
            if self.book_list[i].get_call_number() == call_number and self.book_list[i].check_availability():
                self.book_list[i].set_num_copies(self.book_list[i].get_num_copies()-1)
                return True
            i += 1
        print('Book not found or unavailable.')
        return False

    def return_book(self, call_number):
        i = 0
        while i < len(self.book_list):
            if self.book_list[i].get_call_number() == call_number:
                self.book_list[i].set_num_copies(self.book_list[i].get_num_copies()+1)
                return True
            i += 1
        return False

    def display_available_books(self):
        i = 0
        print('Available books:')
        while i < len(self.book_list):
            print(self.book_list[i])
            i += 1

    def find_books(self, title):
        i = 0
        title_list = []
        while i < len(self.book_list):
            title_list.append(self.book_list[i].get_title())
            if self.book_list[i].get_title() == title:
                return self.book_list[i]
            i += 1
        similar_titles = get_close_matches(title, title_list)
        if not similar_titles:
            print('Book not found, no similar book titles found.')
        else:

            print(f'book not found, do you mean {str(", ").join(similar_titles)}?')


def main():
    book_a = Book('Python101', '1', 'Guy', 3)
    book_b = Book('Python102', '2', 'Guy', 4)
    library = Library([book_a])
    library.add_book(book_b)
    library.find_books('Python101')
    library.display_available_books()
    library.check_out('1')
    library.display_available_books()
    library.return_book('1')
    library.display_available_books()
    library.check_out('1')
    library.display_available_books()
    library.check_out('1')
    library.display_available_books()
    library.check_out('1')
    library.display_available_books()
    library.check_out('1')
    library.display_available_books()
    library.check_out('1')

    library.find_books('python010')


if __name__ == '__main__':
    main()
