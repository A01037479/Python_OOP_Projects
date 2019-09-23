from pet import Pet
from mushroom import Mushroom


class Teemo(Pet):
    def __init__(self):
        super().__init__()
        self.name = 'Teemo'
        self.health_decline_rate = 2
        self.hunger_increase_rate = 0.1
        self.happiness_decline_rate = 0.05
        self.health_standard = 70
        self.favorite_food = Mushroom
        self.message = ['Hump, two, three, four!', 'Captain Teemo on duty!',
                        'Never underestimate the power of the Scout\'s code.']
