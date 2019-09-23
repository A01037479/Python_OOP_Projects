from datetime import datetime
from teemo import Teemo
from fizz import Fizz
from yuumi import Yuumi
from mushroom import Mushroom
from chicken import Chicken
from crabmeat import Crab_meat
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

        print(f'Congrats, a {cls.pet.__class__.__name__} is born!\n')

    @classmethod
    def update_status(cls):
        update_time = datetime.now()
        time_elapsed = (update_time - cls.pet.last_checked_time).total_seconds()
        cls.pet.lower_happiness(time_elapsed)
        cls.pet.lower_health(time_elapsed)
        cls.pet.gain_hunger(time_elapsed)
        if cls.pet.health < cls.pet.health_standard:
            cls.pet.fall_sick()
        if cls.pet.health == 0:
            cls.pet.die()
        cls.pet.last_checked_time = update_time

        if Game.pet.is_dead:
            return False

        return True

    @classmethod
    def check_status(cls):
        print(f'{cls.pet.name} says: {cls.pet.message[random.randint(0,2)]}\n')
        if not cls.update_status():
            return False
        print(cls.pet)
        return True

    @classmethod
    def feed_food(cls):
        food_choice = input(f'What food would you like to feed?\n'
                            f' 1. {Crab_meat.name}\n'
                            f' 2. {Mushroom.name}\n'
                            f' 3. {Chicken.name}\n'
                            f'  :')
        if not cls.update_status():
            return False
        if food_choice == '1':
            Crab_meat.feed(cls.pet)
        elif food_choice == '2':
            Mushroom.feed(cls.pet)
        elif food_choice == '3':
            Chicken.feed(cls.pet)
        else:
            print(f'No such food option!')
        return True

    @classmethod
    def feed_medicine(cls):
        if not cls.update_status():
            return False
        Medicine.feed(cls.pet)
        return True

    @classmethod
    def play_mini_game(cls):
        Mini_games.rock_paper_scissors(cls.pet)
        if not cls.update_status():
            return False
        cls.pet.gain_happiness(cls.pet.happiness_gain)
        return True
