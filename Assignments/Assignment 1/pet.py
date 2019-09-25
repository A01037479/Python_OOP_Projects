from abc import ABC
from datetime import datetime


class Pet(ABC):
    """
    Abstract class that is also super class of Teemo, Yuumi, Fizz.
    It provides properties and structure for its child classes that
    represent specific species of pets.
    """
    def __init__(self):
        self.name = None
        self.birth_date = datetime.now()
        self.last_checked_time = datetime.now()
        self.favorite_food = None
        self.hunger = 0
        self.health = 100
        self.happiness = 100
        self.health_decline_rate = None
        self.hunger_increase_rate = None
        self.happiness_decline_rate = None
        self.health_standard = None
        self.happiness_gain_rate = None
        self.message = None
        self.is_sick = False
        self.is_dead = False

    def get_name(self):
        return self.name

    def get_favorite_food(self):
        return self.favorite_food

    def get_last_checked_time(self):
        return self.last_checked_time

    def get_hunger(self):
        return self.hunger

    def get_health(self):
        return self.health

    def get_happiness(self):
        return self.happiness

    def get_health_decline_rate(self):
        return self.health_decline_rate

    def get_hunger_increase_rate(self):
        return self.hunger_increase_rate

    def get_happiness_decline_rate(self):
        return self.happiness_decline_rate

    def get_health_standard(self):
        return self.health_standard

    def get_happiness_gain_rate(self):
        return self.happiness_gain_rate

    def get_message(self):
        return self.message

    def get_is_sick(self):
        return self.is_sick

    def get_is_dead(self):
        return self.is_dead

    def set_last_checked_time(self, time):
        self.last_checked_time = time

    def lower_health(self, time_elapsed):
        """
        Decrease pet's health based on elapsed time period. Doubles the
        decreased amount when pet's hunger level reaches 100/100
        :param time_elapsed: datetime
        """
        if self.hunger == 100:
            self.health -= int(int(time_elapsed)
                               * self.health_decline_rate * 2)
            self.health = self.valid_stats(self.health)
        else:
            self.health -= int(int(time_elapsed)
                               * self.health_decline_rate)
            self.health = self.valid_stats(self.health)

    def gain_hunger(self, time_elapsed):
        """
        Increases pet's hunger level based on elapsed time period.
        :param time_elapsed: datetime
        """
        self.hunger += int(int(time_elapsed)
                           * self.hunger_increase_rate)
        self.hunger = self.valid_stats(self.hunger)

    def lower_happiness(self, time_elapsed):
        """
        Decreases pet's happiness level based on elapsed time period.
        :param time_elapsed: datetime
        """
        self.happiness -= int(int(time_elapsed)
                              * self.happiness_decline_rate)
        self.happiness = self.valid_stats(self.happiness)

    def reset_health(self):
        """
        Restores pet's health to 100/100
        """
        self.health = 100

    def gain_happiness(self, amount):
        """
        Increases pet's happiness level based on input amount.
        :param amount: int
        """
        self.happiness += amount
        self.happiness = self.valid_stats(self.happiness)

    def lower_hunger(self, amount):
        """
        Decreases pet's hunger level based on input amount.
        :param amount: int
        """
        self.hunger -= amount
        self.hunger = self.valid_stats(self.hunger)

    def fall_sick(self):
        """
        Sets pet to be sick.
        """
        self.is_sick = True

    def recover_health_status(self):
        """
        Sets pet to be healthy.
        """
        self.is_sick = False

    def die(self):
        """
        Sets pet to be dead
        :return:
        """
        self.is_dead = True

    def valid_stats(self, stat):
        """
        Validation helper function to validate stats level in [0, 100]
        :param stat: int
        """
        if stat <= 0:
            stat = 0
        elif stat >= 100:
            stat = 100
        return stat

    def __str__(self):
        return (f'Pet name:         {self.get_name()}\n'
                f'Birth date:       '
                f'{self.birth_date.strftime("%b %d %Y %H:%M:%S")}\n'
                f'Hunger level:     {self.hunger}/100\n'
                f'Happiness level:  {self.happiness}/100\n'
                f'Health level:     {self.health}/100\n'
                f'Health status:    '
                f'{"Sick" if self.is_sick else "Healthy"}\n')
