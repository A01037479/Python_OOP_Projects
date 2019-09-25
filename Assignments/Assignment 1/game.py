import time
from datetime import datetime
from teemo import Teemo
from fizz import Fizz
from yuumi import Yuumi
from food import Food
from medicine import Medicine
from minigames import Mini_games
import random


class Game:
    """
    Static class that represents the game. The game provides methods
    that represents player options.
    """
    pet = None

    @classmethod
    def hatch(cls):
        """
        Randomly create a pet object, from Teemo, Fizz or Yuumi
        """
        hatch_code = random.randint(1, 3)
        if hatch_code == 1:
            cls.pet = Teemo()
        elif hatch_code == 2:
            cls.pet = Fizz()
        elif hatch_code == 3:
            cls.pet = Yuumi()
        i = 0
        while i < 3:
            print('Hatching...')
            time.sleep(1)
            i += 1
        print(f'Congrats, a {cls.pet.get_name()} is born!\n')

    @classmethod
    def update_status(cls):
        """
        Helper method that is called when an action is done to the pet.
        It renews pet's status.
        """
        update_time = datetime.now()
        time_elapsed = (update_time - cls.pet.get_last_checked_time()) \
            .total_seconds()
        cls.pet.lower_happiness(time_elapsed)
        cls.pet.lower_health(time_elapsed)
        cls.pet.gain_hunger(time_elapsed)
        if cls.pet.get_health() < cls.pet.get_health_standard():
            cls.pet.fall_sick()
        if cls.pet.get_health() == 0:
            cls.pet.die()
        cls.pet.set_last_checked_time(update_time)
        if Game.pet.get_is_dead():
            return False
        return True

    @classmethod
    def check_status(cls):
        """
        The method prints out pet's status at the moment
        """
        if not cls.update_status():
            return False
        print(f'{cls.pet.get_name()} says:'
              f' {cls.pet.get_message()[random.randint(1, 3)]}\n')
        print(cls.pet)
        return True

    @classmethod
    def feed_food(cls):
        """
        Takes in user input of food choice from three, and feeds food
        to the pet to lower its hunger level
        """
        food_choice = input(f'What food would you like to feed?\n'
                            f' 1. {Food.food_dct["1"]}\n'
                            f' 2. {Food.food_dct["2"]}\n'
                            f' 3. {Food.food_dct["3"]}\n'
                            f'  :')
        if not cls.update_status():
            return False
        if int(food_choice) in range(1, 4):
            Food.feed(cls.pet, food_choice)
            if Food.food_dct[food_choice] == cls.pet.get_favorite_food():
                print(f'{cls.pet.get_name()} says: '
                      f'{cls.pet.get_message()["after_fav_food_msg"]}'
                      f' (pet hunger level is now '
                      f'{cls.pet.get_hunger()}/100)\n')
            else:
                print(f'{cls.pet.get_name()} says: '
                      f'{cls.pet.get_message()["after_food_msg"]}'
                      f' (pet hunger level is now '
                      f'{cls.pet.get_hunger()}/100)\n')
        else:
            print(f'No such food option!\n')
        return True

    @classmethod
    def feed_medicine(cls):
        """
        Takes in user input of medicine choice from three, and feeds
        medicine to the pet to reset its health level back to 100/100
        """
        medicine_choice = input(f'Which medicine would you choose?\n'
                                f' 1. {Medicine.medicine_dict["1"]}\n'
                                f' 2. {Medicine.medicine_dict["2"]}\n'
                                f' 3. {Medicine.medicine_dict["3"]}\n'
                                f'  :')
        if not cls.update_status():
            return False
        if medicine_choice in ['1', '2', '3']:
            Medicine.feed(cls.pet)
            print(f'{cls.pet.get_name()} says: '
                  f'{cls.pet.get_message()["after_medicine_msg"]}'
                  f' (pet health is now 100/100)\n')
        else:
            print('No such medicine choice!\n')
        return True

    @classmethod
    def play_mini_game(cls):
        """
        Takes in user input of mini game choice from three, and run the
        game methods to increase pet's happiness level
        """
        game_choice = input(
            f'What game would you like to play with your'
            f' {cls.pet.get_name()}?\n'
            f' 1. Rock, paper and scissors\n'
            f' 2. Hide and seek\n'
            f'  :')
        if game_choice == '1':
            Mini_games.rock_paper_scissors()
            print(f'{cls.pet.get_name()} says: '
                  f'{cls.pet.get_message()["after_game_msg"]}'
                  f'(pet happiness is now {cls.pet.get_happiness()}/100)\n')
        elif game_choice == '2':
            Mini_games.hide_and_seek()
            print(f'{cls.pet.get_name()} says: '
                  f'{cls.pet.get_message()["after_game_msg"]}'
                  f'(pet happiness is now {cls.pet.get_happiness()}/100)\n')
        else:
            print('No such game option!\n')
        if not cls.update_status():
            return False
        cls.pet.gain_happiness(cls.pet.get_happiness_gain_rate())
        return True
