from catalogue import Catalogue


class Library:
    """
    A class represents library
    """
    def __init__(self, catalogue):
        """
        Initialize a library
        :param catalogue: a catalogue that contains items
        """
        self.catalogue = catalogue

    def check_out(self, call_number):
        """
        Checks out an item from library
        :param call_number: A string that uniquely identifies item
        :return: True if item founded, False otherwise
        """
        for item in self.catalogue.item_list:
            if item.call_number == call_number and item.check_availability():
                item.num_copies = int(item.num_copies) - 1
                print('Item checked out!')
                return True
        print('Item not found or unavailable.')
        return False

    def return_item(self, call_number):
        """
        Returns an item to library
        :param call_number:  A string that uniquely identifies item
        :return: True if item founded, False otherwise
        """
        for item in self.catalogue.item_list:
            if item.call_number == call_number:
                item.num_copies = int(item.num_copies) + 1
                print('Item returned!')
                return True
        return False


def main():
    """
    Main method that drives the program.
    Creates a menu for users to interact with library
    """
    catalogue = Catalogue()
    library = Library(catalogue)
    stop = False
    while not stop:
        user_input = input("\nWelcome to BCIT library\n"
                           "1. Add items to catalogue\n"
                           "2. Remove items from catalogue\n"
                           "3. Search for items in catalogue\n"
                           "4. Check out an item\n"
                           "5. Return an item\n"
                           "6. Display all available items\n"
                           "7. Stop the program\n"
                           ": ")
        if user_input == '1':
            library.catalogue.add_item()
        elif user_input == '2':
            call_num = input('Enter item call number: ')
            library.catalogue.remove_item(call_num)
        elif user_input == '3':
            title = input('Enter item title: ')
            library.catalogue.find_item(title)
        elif user_input == "4":
            call_num = input('Enter item call number: ')
            library.check_out(call_num)
        elif user_input == '5':
            call_num = input('Enter item call number: ')
            library.return_item(call_num)
        elif user_input == '6':
            library.catalogue.display_available_items()
        elif user_input == '7':
            stop = True
        else:
            print('Invalid input, try again.')


if __name__ == '__main__':
    main()
