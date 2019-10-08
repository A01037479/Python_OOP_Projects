from card_manager import CardManager
from card_generator import CardGenerator


class Controller:
    card_manager = None

    @classmethod
    def start_app(cls):
        cls.card_manager = CardManager()
        user_input = input(f'1. Add a card\n'
                           f'2. Remove a card\n'
                           f'3. View cards by type\n'
                           f'4. Back up data\n'
                           f'5. Exit app\n'
                           f'   : ')
        if user_input == '1':
            Controller.user_add_card()
        elif user_input == '2':
            Controller.user_remove_card()

    @classmethod
    def end_app(cls):
        sys.exit()

    @classmethod
    def user_add_card(cls):
        card_type = input(f' Enter card type:\n'
                          f' 1. Loyalty Card\n'
                          f' 2. Membership Card\n'
                          f' 3. Gift Card\n'
                          f' 4. Debit Card\n'
                          f' 5. Credit Card\n'
                          f' 6. Employee Card\n'
                          f' 7. Student Card\n'
                          f'    :')
        if int(card_type) not in range(1, 8):
            return False
        card_name = input(' Enter card name: ')
        card_holder = input(' Enter card holder name: ')
        issued_by = input(' Issued by: ')
        if int(card_type) in range(5, 8):
            issue_date = input(' Enter issue date: ')
            expiry_date = input(' Enter expiry date: ')
        if card_type == '1':
            new_card = CardGenerator.create_dedit_card(card_name, card_holder,
                                                       issued_by)
        elif card_type == '2':

            new_card = CardGenerator.create_credit_card(card_name, card_holder,
                                                        issued_by, issue_date,
                                                        expiry_date, )
        cls.card_manager.add_card(new_card)
        cls.card_manager.view_card_by_type('StudentCard')

    @classmethod
    def user_remove_card(cls):
        pass


def main():
    """
    Main method that drives the program.
    """
    Controller.start_app()


if __name__ == '__main__':
    main()
