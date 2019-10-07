from card_manager import CardManager


class controller:
    card_manager = None

    @classmethod
    def start_app(cls):
        cls.card_manager = CardManager()

    @classmethod
    def show_menu(cls):
        print('123')

    @classmethod
    def end_app(cls):
        sys.exit()