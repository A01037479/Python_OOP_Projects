from datetime import datetime


class Pet:
    def __init__(self):
        self.birth_date = datetime.now()
        self.last_checked_time = datetime.now()
        self.hunger = 0
        self.health = 100
        self.happiness = 100
        self.health_decline_rate = None
        self.hunger_increase_rate = None
        self.happiness_decline_rate = None
        self.health_standard = None
        self.happiness_gain = 5
        self.is_sick = False
        self.is_dead = False

    def lower_health(self, time_elapsed):
        if self.hunger == 100:
            self.health -= int(int(time_elapsed) * self.health_decline_rate * 2)
            self.health = self.valid_stats(self.health)
        else:
            self.health -= int(int(time_elapsed) * self.health_decline_rate)
            self.health = self.valid_stats(self.health)

    def gain_hunger(self, time_elapsed):
        self.hunger += int(int(time_elapsed) * self.hunger_increase_rate)
        self.hunger = self.valid_stats(self.hunger)

    def lower_happiness(self, time_elapsed):
        self.happiness -= int(int(time_elapsed) * self.happiness_decline_rate)
        self.happiness = self.valid_stats(self.happiness)

    def reset_health(self):
        self.health = 100

    def gain_happiness(self, amount):
        self.happiness += amount
        self.happiness = self.valid_stats(self.happiness)

    def lower_hunger(self, amount):
        self.hunger -= amount
        self.hunger = self.valid_stats(self.hunger)

    def fall_sick(self):
        self.is_sick = True

    def die(self):
        self.is_dead = True

    def valid_stats(self, stat):
        if stat <= 0:
            stat = 0
        elif stat >= 100:
            stat = 100
        return stat

    def __str__(self):
        return (f'Pet name: {self.__class__.__name__}\n'
                f'Birth date: {self.birth_date.strftime("%b %d %Y %H:%M:%S")}\n'
                f'Hunger level: {self.hunger}\n'
                f'Happiness level: {self.happiness}\n'
                f'Health level: {self.health}\n'
                f'Health status: {"Sick" if self.is_sick else "Healthy"}\n')
