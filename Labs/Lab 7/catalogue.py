from difflib import get_close_matches
from item_factory import ItemGenerator


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
        item_generator = ItemGenerator()
        try:
            item_factory = item_generator.generate_item_factory()
            item = item_factory.create_item()
        except AttributeError:
            print('')
        else:
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

