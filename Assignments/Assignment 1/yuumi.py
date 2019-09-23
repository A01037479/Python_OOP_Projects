from pet import Pet
from chicken import Chicken


class Yuumi(Pet):
    def __init__(self):
        super().__init__()
        self.name = 'Yuumi'
        self.health_decline_rate = 4
        self.hunger_increase_rate = 0.08
        self.happiness_decline_rate = 0.06
        self.health_standard = 50
        self.favorite_food = Chicken
        self.message = ['Who\'s ready to risk our lives, defeat our foes, and maybe knock over some cups?',
                        'Tell me the game plan again. Wait. Fish! Someone has fish! Where is it?',
                        'Cats make great companions! Just ask my master...'
                        ' who disappeared under mysterious circumstances.']

