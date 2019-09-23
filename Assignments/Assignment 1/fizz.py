from pet import Pet
from crabmeat import Crab_meat


class Fizz(Pet):
    def __init__(self):
        super().__init__()
        self.fizz = 'Fizz'
        self.health_decline_rate = 3
        self.hunger_increase_rate = 0.15
        self.happiness_decline_rate = 0.1
        self.health_standard = 60
        self.favorite_food = Crab_meat
        self.message = ['To the briny deep', 'The mighty shark stalks his prey.',
                        'I\'ll show them a watery grave.']
