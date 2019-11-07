from difflib import get_close_matches
from item import Book, DVD, Journal


class Catalogue:
    """
    A class that represents a catalogue of library, contains a list of items
    """

    def __init__(self):
        """
        initializes a catalogue
        """
        self.item_list = {}

    def add_item(self):
        """
        Add items to catalogue
        """
        item = LibraryItemGenerator.create_item()
        if not item:
            return False
        if item.call_number in self.item_list.keys():
            print(f'call number {item.call_number} already exists')
            print('Item not added.')
            return False
        if item not in self.item_list.values():
            self.item_list[item.call_number] = item
            print('Item added.')

    def remove_item(self, call_number):
        """
        Remove items by call numbers from catalogue
        :param call_number: unique identifier of an item
        :return: True if item founded, False otherwise
        """
        for item in self.item_list.values():
            if item.call_number == call_number:
                self.item_list.pop(item.call_number)
                print('Item removed.')
                return True
        print('Item not found.')
        return False

    def find_item(self, title):
        """
        Searches for items by item title from catalogue
        :param title: title of an item
        :return: True the item if founded
        """
        title_list = []

        for item in self.item_list.values():
            title_list.append(item.get_title())
            if item.get_title() == title:
                print(f'Item found, {item}')
                return item
        similar_titles = get_close_matches(title, title_list)
        if not similar_titles:
            print('Item not found, no similar item found.')
        else:
            print(
                f'Item not found, do you mean {str(", ").join(similar_titles)}?')

    def display_available_items(self):
        """
        Prints all the items from catalogue
        """
        print('Available items:')
        for item in self.item_list.values():
            print(item)


class LibraryItemGenerator:
    """
    A static class that helps generates library items
    """

    @staticmethod
    def create_item():
        """
        A static method to prompt users information to create items
        :return: item
        """
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
            item = DVD(title, call_number, num_copies, release_date,
                       region_code)
        elif item_type == 'journal':
            author = input(f"Enter {item_type} author: ")
            issue_number = input(f"Enter {item_type} issue number: ")
            publisher = input(f"Enter {item_type} publisher: ")
            item = Journal(title, call_number, author, num_copies,
                           issue_number, publisher)
        return item