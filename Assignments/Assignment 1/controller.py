import sys

from game import Game


class Controller:
    @staticmethod
    def start_game():
        print('Welcome to Tamagotchi League of Legends edition!')
        while 1:
            print('Would you like to start hatching an egg now?')
            user_input = input(' 1. Yes, hatch it!\n'
                               ' 2. No, exit game.\n'
                               '  : ')
            if user_input == "1":
                Game.hatch()
                Controller.proceed_game()
            elif user_input == '2':
                Controller.end_game()
            else:
                print('Invalid option.')

    @staticmethod
    def proceed_game():
        pet_name = Game.pet.get_name()
        continue_game = True
        while continue_game:
            user_input = input(f'What would you like to do?\n'
                               f' 1. Check status of {pet_name}\n'
                               f' 2. Feed {pet_name}\n'
                               f' 3. Provide medicine to {pet_name}\n'
                               f' 4. Play mini games with {pet_name}\n'
                               f' 5. Exit game.\n'
                               f'  :')
            if user_input == '1':
                continue_game = Game.check_status()
            elif user_input == '2':
                continue_game = Game.feed_food()
            elif user_input == '3':
                continue_game = Game.feed_medicine()
            elif user_input == '4':
                continue_game = Game.play_mini_game()
            elif user_input == '5':
                Controller.end_game()
            else:
                print('Invalid choice!')
        Controller.restart_game()

    @staticmethod
    def restart_game():
        user_input = input(f'{Game.pet.get_name()} has died :( \n'
                           f'Would you like to start over '
                           f'and hatch a new egg?\n'
                           f' 1. Yes, start a new game! \n'
                           f' 2. No, exit game.\n'
                           f'  : ')
        if user_input == '1':
            Controller.start_game()
        elif user_input == '2':
            Controller.end_game()
        else:
            Controller.restart_game()

    @staticmethod
    def end_game():
        sys.exit()


def main():
    """
    Main method that drives the program.
    """
    Controller.start_game()


if __name__ == '__main__':
    main()
