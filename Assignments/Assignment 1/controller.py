import sys

from game import Game


class Controller:
    @staticmethod
    def start_game():
        print('Welcome to Tamagotchi League of Legends edition!\n'
              'Would you like to start hatching an egg now?')
        user_input = int(input(' 1. Yes, hatch it!\n'
                               ' 2. No, exit game.\n'
                               '  : '))

        Game.hatch() if user_input == 1 else Controller.end_game()
        Controller.proceed_game()

    @staticmethod
    def proceed_game():
        pet_name = Game.pet.__class__.__name__
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
        Controller.restart()

    @staticmethod
    def restart():
        user_input = input(f'{Game.pet.__class__.__name__} has died :( \n'
                           f'Would you like to start over and hatch a new egg?\n'
                           f' 1. Yes, start a new game! \n 2. No, exit game.\n'
                           f'  : ')
        if user_input == '1':
            Controller.start_game()
        else:
            Controller.end_game()

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
