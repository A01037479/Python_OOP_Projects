from catalogue import Catalogue


class Library:
    def __init__(self, catalogue):
        self.catalogue = catalogue

    def check_out(self, call_number):
        i = 0
        while i < len(self.catalogue.item_list):
            if self.catalogue.item_list[i].get_call_number() == call_number \
                    and self.catalogue.item_list[i].check_availability():
                self.catalogue.item_list[i].set_num_copies(int(self.catalogue.item_list[i].get_num_copies()) - 1)
                print('Item checked out!')
                return True
            i += 1
        print('Item not found or unavailable.')
        return False

    def return_book(self, call_number):
        i = 0
        while i < len(self.catalogue.item_list):
            if self.catalogue.item_list[i].get_call_number() == call_number:
                self.catalogue.item_list[i].set_num_copies(int(self.catalogue.item_list[i].get_num_copies()) + 1)
                return True
            i += 1
        return False


def main():
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
            library.return_book(call_num)
        elif user_input == '6':
            library.catalogue.display_available_items()
        elif user_input == '7':
            stop = True
        else:
            print('Invalid input, try again.')


if __name__ == '__main__':
    main()
