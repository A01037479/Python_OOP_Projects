from datetime import datetime
from teemo import Teemo
from fizz import Fizz
from yuumi import Yuumi
from food import Food
from medicine import Medicine
from minigames import Mini_games
import random


class Game:
    pet = None

    @classmethod
    def hatch(cls):
        hatch_code = random.randint(1, 3)
        if hatch_code == 1:
            cls.pet = Teemo()
        elif hatch_code == 2:
            cls.pet = Fizz()
        elif hatch_code == 3:
            cls.pet = Yuumi()
        """
        i = 0
        while i < 3:
            print('Hatching...')
            time.sleep(1)
            i += 1
        """

        print(f'Congrats, a {cls.pet.get_name()} is born!\n')

    @classmethod
    def update_status(cls):
        update_time = datetime.now()
        time_elapsed = (update_time - cls.pet.get_last_checked_time()).total_seconds()
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
        if not cls.update_status():
            return False
        print(f'{cls.pet.get_name()} says: {cls.pet.get_message()[random.randint(1, 3)]}\n')
        print(cls.pet)
        return True

    @classmethod
    def feed_food(cls):
        food_choice = input(f'What food would you like to feed?\n'
                            f' 1. Mushroom\n'
                            f' 2. Crab Meat\n'
                            f' 3. Chicken\n'
                            f'  :')
        if not cls.update_status():
            return False
        if int(food_choice) in range(1, 4):
            Food.feed(cls.pet, Food.food_dct[food_choice])
            if Food.food_dct[food_choice] == cls.pet.get_favorite_food():
                print(f'{cls.pet.get_name()} says: {cls.pet.get_message()["after_fav_food_msg"]}'
                      f' (pet hunger level is now {cls.pet.get_hunger()}/100)\n')
            else:
                print(f'{cls.pet.get_name()} says: {cls.pet.get_message()["after_food_msg"]}'
                      f' (pet hunger level is now {cls.pet.get_hunger()}/100)\n')
        else:
            print(f'No such food option!')
        return True

    @classmethod
    def feed_medicine(cls):
        if not cls.update_status():
            return False
        Medicine.feed(cls.pet)
        print(f'{cls.pet.get_name()} says: {cls.pet.get_message()["after_medicine_msg"]}'
              f' (pet health is now 100/100)\n')
        return True

    @classmethod
    def play_mini_game(cls):
        game_choice = input(f'What game would you like to play with your {cls.pet.get_name()}?\n'
                            f' 1. Rock, paper and scissors\n'
                            f' 2. Hide and seek\n'
                            f'  :')
        if game_choice == '1':
            Mini_games.rock_paper_scissors()
        else:
            Mini_games.hide_and_seek()
        if not cls.update_status():
            return False
        cls.pet.gain_happiness(cls.pet.get_happiness_gain_rate())
        print(f'{cls.pet.get_name()} says: {cls.pet.get_message()["after_game_msg"]}'
              f'(pet happiness is now {cls.pet.get_happiness()}/100)\n')
        return True
