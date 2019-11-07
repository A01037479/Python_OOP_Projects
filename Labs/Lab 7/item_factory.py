"""
This module contains the factory pattern to generate
different kinds of items for a library
"""
from item import Item, Book, DVD, Journal
import abc


class ItemFactory(abc.ABC):
    """
    Defines an ItemFactory interface that the rest of the factories depends on.
    It describes a factory that creates an item.
    """
    @staticmethod
    def get_kwargs():
        """
        Returns a container of user inputs for code re-use.
        :return: dict
        """
        return {'title': input(f"Enter title: "),
                'call_number': input(f"Enter call number: "),
                'num_copies': input(f"Enter number of copies: ")}

    @abc.abstractmethod
    def create_item(self) -> Item:
        pass


class BookFactory(ItemFactory):
    """
    The BookFactory is responsible for creating a Book item.
    """
    def create_item(self) -> Item:
        kwargs = ItemFactory.get_kwargs()
        return Book(**kwargs, author=input(f"Enter author: "))


class DvdFactory(ItemFactory):
    """
    The DvdFactory is responsible for creating a DVD item.
    """
    def create_item(self) -> Item:
        kwargs = ItemFactory.get_kwargs()
        return DVD(**kwargs, release_date=input(f"Enter release date: "),
                   region_code=input(f"Enter region code: "))


class JournalFactory(ItemFactory):
    """
    The JournalFactory is responsible for creating a Journal item.
    """
    def create_item(self) -> Item:
        kwargs = ItemFactory.get_kwargs()
        return Journal(**kwargs, author=input(f"Enter author: "),
                       issue_number=input(f"Enter issue number: "),
                       publisher=input(f"Enter publisher: "))


class ItemGenerator:
    """
    The ItemGenerator is responsible for taking in user choices of item type
    and create corresponding items.
    """
    def __init__(self):
        self.item_choice = {
            'book': BookFactory,
            'dvd': DvdFactory,
            'journal': JournalFactory
        }

    def generate_item_factory(self) -> ItemFactory:
        try:
            item_type = input("Enter item type: ").upper().lower().strip()
            item_factory = self.item_choice[item_type]()
        except KeyError:
            print('Incorrect item type!')
        else:
            return item_factory
