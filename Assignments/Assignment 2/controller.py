import sys

from card_manager import CardManager
from card_generator import CardGenerator
from card import Expirable, IDCard


class Controller:
    card_manager = None

    @classmethod
    def start_app(cls):
        cls.card_manager = CardManager()
        while True:
            user_input = input(f'1. Add a card\n'
                               f'2. Remove a card\n'
                               f'3. View all cards\n'
                               f'4. View cards by type\n'
                               f'5. Back up data\n'
                               f'6. Exit app\n'
                               f'   : ')
            if user_input == '1':
                Controller.user_add_card()
            elif user_input == '2':
                Controller.user_remove_card()
            elif user_input == '3':
                Controller.card_manager.view_all_cards()
            elif user_input == '6':
                Controller.end_app()

    @classmethod
    def end_app(cls):
        sys.exit()

    @classmethod
    def user_add_card(cls):
        print('Enter card type:')

        for key, card_type in CardGenerator.card_str_type_dict.items():
            print(f'{key}: {card_type}')

        card_type_key = input(': ')

        if card_type_key not in CardGenerator.card_type_dict.keys():
            print('No such card type option!\n')
            return False

        print(f'Adding a new {CardGenerator.card_str_type_dict[card_type_key]}: ')
        card_name = input(' Enter card name: ')
        card_holder = input(' Enter card holder name: ')
        issued_by = input(' Issued by: ')
        new_card = None
        expiry_date = None
        issue_date = None
        id_number = None

        if issubclass(CardGenerator.card_type_dict[card_type_key], Expirable):
            issue_date = input(' Enter issue date: ')
            expiry_date = input(' Enter expiry date: ')

        if issubclass(CardGenerator.card_type_dict[card_type_key], IDCard):
            id_number = input(' Enter card ID number: ')

        if card_type_key == '1':
            reward_type = input(' Enter reward type(stamps/points/other): ')
            new_card = CardGenerator.create_reward_card(card_name, card_holder,
                                                        issued_by, reward_type)
        elif card_type_key == '2':
            balance = input(' Enter card balance: ')
            new_card = CardGenerator.create_balance_card(card_name,
                                                         card_holder,
                                                         issued_by, balance)
        elif card_type_key == '3':
            membership_level = input(' Enter membership_level: ')
            new_card = CardGenerator.create_membership_card \
                (card_name, card_holder, issued_by, issue_date, expiry_date,
                 membership_level)
        elif card_type_key == '4':
            bank_info = input(' Enter bank information: ')
            new_card = CardGenerator.create_bank_card(card_name, card_holder,
                                                      issued_by, issue_date,
                                                      expiry_date, bank_info)
        elif card_type_key == '5':
            new_card = CardGenerator.create_id_card(card_name, card_holder,
                                                    issued_by, issue_date,
                                                    expiry_date, id_number)
        elif card_type_key == '6':
            personal_information = input(' Enter personal information: ')
            new_card = CardGenerator.create_gov_id_card \
                (card_name, card_holder, issued_by, issue_date,
                 expiry_date, id_number, personal_information)
        elif card_type_key == '7':
            card_description = input(' Enter card description: ')
            new_card = CardGenerator.create_other(card_name, card_holder,
                                                  issued_by, card_description)

        cls.card_manager.add_card(new_card)
        print(
            f'{new_card.card_name} is successfully added to card manager! \n')

    @classmethod
    def user_remove_card(cls):
        card_name = input('Enter card name of the card to be removed: ')
        for card in Controller.card_manager.cards:
            if card.card_name == card_name:
                cls.card_manager.remove_card(card)
                print(f'Card {card_name} removed!\n')
                return


def main():
    """
    Main method that drives the program.
    """
    Controller.start_app()


if __name__ == '__main__':
    main()
