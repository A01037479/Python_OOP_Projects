from difflib import get_close_matches
from item import Item
from book import Book
from dvd import DVD
from journal import Journal


class Catalogue:
    def __init__(self):
        self.item_list = []

    def add_item(self):
        item = LibraryItemGenerator.create_item()
        if item not in self.item_list:
            self.item_list.append(item)

    def remove_item(self, call_number):
        i = 0
        while i < len(self.item_list):
            if self.item_list[i].get_call_number() == call_number:
                self.item_list.remove(self.item_list[i])
                print('Item removed.')
                return True
            i += 1
        print('Item not found.')
        return False

    def find_item(self, title):
        i = 0
        title_list = []
        while i < len(self.item_list):
            title_list.append(self.item_list[i].get_title())
            if self.item_list[i].get_title() == title:
                print(f'Item found, {self.item_list[i]}')
                return self.item_list[i]
            i += 1
        similar_titles = get_close_matches(title, title_list)
        if not similar_titles:
            print('Item not found, no similar item found.')
        else:

            print(f'Item not found, do you mean {str(", ").join(similar_titles)}?')

    def display_available_items(self):
        print('Available items:')
        for item in self.item_list:
            print(item)


class LibraryItemGenerator:

    @staticmethod
    def create_item():
        item_type = input("Enter item type: ").upper().lower().strip()
        if item_type in ['book', 'dvd', 'journal']:
            title = input(f"Enter {item_type} title: ")
            call_number = input(f"Enter {item_type} call number: ")
            num_copies = input(f"Enter {item_type} number of copies: ")
        else:
            print('invalid item type')
            return False
        if item_type == 'book':
            author = input(f"Enter {item_type} author: ")
            item = Book(title, call_number, author, num_copies)
        elif item_type == 'dvd':
            release_date = input(f"Enter {item_type} release date: ")
            region_code = input(f"Enter {item_type} region code: ")
            item = DVD(title, call_number, num_copies, release_date, region_code)
        elif item_type == 'journal':
            author = input(f"Enter {item_type} author: ")
            issue_number = input(f"Enter {item_type} issue number: ")
            publisher = input(f"Enter {item_type} publisher: ")
            item = Journal(title, call_number, author, num_copies, issue_number, publisher)
        print('Item added.')
        return item
