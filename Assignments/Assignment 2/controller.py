"""
The module contains Controller class that interacts with user and card manger.
It has main method that drives the program.
"""
import datetime
import sys

from card_manager import CardManager
from card import Expirable, IDCard
from exception import InvalidCardTypeError, InvalidCardBalanceError, \
    InvalidDateFormatError, DuplicatedNameError, NameNotFoundError, \
    EmptyCardManagerError, InvalidSexError, InvalidHeightError, InvalidAgeError


class Controller:
    """
    The controller class contains a card manager and make interaction between
    it and users.
    """
    card_manager = None

    @classmethod
    def start_app(cls):
        """
        Starts the application by prompting user menu.
        Catches all kinds of exceptions if raised.
        """
        cls.card_manager = CardManager()
        menu_dict = {1: Controller.user_add_card,
                     2: Controller.user_remove_card,
                     3: Controller.user_view_all_card,
                     4: Controller.user_view_card,
                     5: Controller.user_search_card,
                     6: Controller.user_backup_data,
                     7: Controller.end_app}
        while True:
            try:
                user_input = int(input(f'1. Add a card\n'
                                       f'2. Remove a card\n'
                                       f'3. View all cards\n'
                                       f'4. View cards by type\n'
                                       f'5. Search for a card\n'
                                       f'6. Back up data\n'
                                       f'7. Exit app\n'
                                       f'   : '))
                menu_dict[user_input]()
            except KeyError:
                print(f'Invalid option\nPlease enter integer 1 to 7!\n')
            except ValueError:
                print(f'Invalid option\nPlease enter integers only!\n')
            except InvalidCardBalanceError as e:
                print(f'InvalidCardBalanceError caught! {e}')
            except InvalidCardTypeError as e:
                print(f'InvalidCardTypeError caught! {e}')
            except InvalidDateFormatError as e:
                print(f'InvalidDateFormatError caught! {e}')
            except DuplicatedNameError as e:
                print(f'DuplicatedNameError caught! {e}')
            except NameNotFoundError as e:
                print(f'NameNotFoundError caught! {e}')
            except EmptyCardManagerError as e:
                print(f'EmptyCardManagerError caught! {e}')
            except InvalidAgeError as e:
                print(f'InvalidAgeError caught! {e}')
            except InvalidHeightError as e:
                print(f'InvalidHeightError caught! {e}')
            except InvalidSexError as e:
                print(f'InvalidSexError caught! {e}')
            except TypeError as e:
                print(f'InvalidFileTypeError caught! {e}')

    @classmethod
    def end_app(cls):
        sys.exit()

    @classmethod
    def user_add_card(cls):
        """
        Prompts for user inputs to create a card and add it to card manager.
        """
        print('Enter card type:')

        for key, card_type in CardManager.card_str_type_dict.items():
            print(f'{key}: {card_type}')

        try:
            card_type_key = int(input(': '))
        except ValueError:
            raise InvalidCardTypeError

        if card_type_key not in CardManager.card_type_dict.keys():
            raise InvalidCardTypeError

        print(
            f'Adding a new {CardManager.card_str_type_dict[card_type_key]}: ')

        card_name = input(' Enter card name: ')
        if len(card_name) == 0:
            print('Card name cannot be empty!\n')
            return
        for card in cls.card_manager.cards:
            if card_name == Controller.card_manager.card_name(card):
                raise DuplicatedNameError

        card_holder = input(' Enter card holder name: ')
        issued_by = input(' Issued by: ')
        expiry_date = None
        issue_date = None
        id_number = None
        new_card = None
        date_format = '%Y-%m-%d'
        if issubclass(CardManager.card_type_dict[card_type_key],
                      Expirable):
            issue_date = input(' Enter issue date(YYYY-MM-DD): ')
            try:
                datetime.datetime.strptime(issue_date, date_format)
            except ValueError:
                raise InvalidDateFormatError
            expiry_date = input(' Enter expiry date(YYYY-MM-DD): ')
            try:
                datetime.datetime.strptime(expiry_date, date_format)
            except ValueError:
                raise InvalidDateFormatError

        if issubclass(CardManager.card_type_dict[card_type_key], IDCard):
            id_number = input(' Enter card ID number: ')

        if card_type_key == 1:
            reward_type = input(
                ' Enter reward type(e.g. stamps/points): ')
            new_card = CardManager.create_reward_card(card_name,
                                                      card_holder,
                                                      issued_by,
                                                      reward_type)
        elif card_type_key == 2:
            try:
                balance = int(input(' Enter card balance: '))
            except ValueError:
                raise InvalidCardBalanceError
            if balance < 0:
                raise InvalidCardBalanceError
            new_card = CardManager.create_balance_card(card_name,
                                                       card_holder,
                                                       issued_by, balance)
        elif card_type_key == 3:
            membership_level = input(' Enter membership_level(e.g. vip): ')
            new_card = CardManager.create_membership_card \
                (card_name, card_holder, issued_by, issue_date,
                 expiry_date,
                 membership_level)
        elif card_type_key == 4:
            bank_info = input(' Enter bank information(e.g. address): ')
            new_card = CardManager.create_bank_card(card_name, card_holder,
                                                    issued_by, issue_date,
                                                    expiry_date, bank_info)
        elif card_type_key == 5:
            new_card = CardManager.create_id_card(card_name, card_holder,
                                                  issued_by, issue_date,
                                                  expiry_date, id_number)
        elif card_type_key == 6:
            print(' Enter following personal information: ')
            try:
                age = int(input(' Enter age(0-99): '))
            except ValueError:
                raise InvalidAgeError
            else:
                if age < 0 or age > 100:
                    raise InvalidAgeError

            try:
                height = float(input(' Enter height(cm): '))
            except ValueError:
                raise InvalidHeightError
            else:
                if height < 0:
                    raise InvalidHeightError

            sex = input(' Enter sex(male/female): ')
            if sex.lower() not in ['male', 'female']:
                raise InvalidSexError

            personal_information = {'age': age, 'sex': sex, 'height': height}
            new_card = CardManager.create_gov_id_card \
                (card_name, card_holder, issued_by, issue_date,
                 expiry_date, id_number, personal_information)
        elif card_type_key == 7:
            card_description = input(' Enter card description: ')
            new_card = CardManager.create_other(card_name, card_holder,
                                                issued_by,
                                                card_description)

        cls.card_manager.add_card(new_card)
        print(
            f'{Controller.card_manager.card_name(new_card)} '
            f'is successfully added to card manager! \n')

    @classmethod
    def user_remove_card(cls):
        """
        Prompts for user input to remove a specified card from card manager.
        """
        found = False
        card_name = input('Enter card name of the card to be removed: ')
        for card in Controller.card_manager.cards:
            if Controller.card_manager.card_name(card) == card_name:
                found = True
                cls.card_manager.remove_card(card)
                print(f'Card {card_name} removed!\n')
        if not found:
            raise NameNotFoundError
        else:
            return True

    @classmethod
    def user_view_all_card(cls):
        """
        Prints out all cards information from card manager.
        """
        if len(cls.card_manager.cards) == 0:
            raise EmptyCardManagerError
        cls.card_manager.view_all_cards()

    @classmethod
    def user_view_card(cls):
        """
        Prompts for user input and prints certain type of cards.
        """
        for item in CardManager.card_str_type_dict.items():
            print(f'{item[0]}: {item[1]}')
        try:
            card_type = int(input('Enter card type to view: '))
        except ValueError:
            raise InvalidCardTypeError
        else:
            cls.card_manager.view_card_by_type(card_type)

    @classmethod
    def user_search_card(cls):
        """
        Prompts for user input to search a specified card from card manager.
        """
        found = False
        card_name = input('Enter the name of the card to be searched: ')
        for card in Controller.card_manager.cards:
            if Controller.card_manager.card_name(card) == card_name:
                found = True
                print(card)
        if not found:
            raise NameNotFoundError
        else:
            return True

    @classmethod
    def user_backup_data(cls):
        """
        Backs up all card data from card manager into a txt file.
        """
        if len(cls.card_manager.cards) == 0:
            raise EmptyCardManagerError
        current_time = datetime.datetime.now().strftime("%d%m%Y_%H%M")
        file_path = f'CardManager_Export_{current_time}.txt'
        cls.card_manager.back_up_data(file_path)
        print(f'All data backed up in file path: {file_path}')
        return True


def main():
    """
    Main method that drives the program.
    """
    Controller.start_app()


if __name__ == '__main__':
    main()
