from pet import Pet


class Yuumi(Pet):
    """
    Yuumi class is a sub class of Pet. A Yuumi is one species of pets.
    It inherits all the properties and methods from parent class.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Yuumi'
        self.health_decline_rate = 4
        self.hunger_increase_rate = 0.8
        self.happiness_decline_rate = 0.6
        self.health_standard = 50
        self.happiness_gain_rate = 10
        self.favorite_food = 'Chicken'
        self.message = {1: 'Who\'s ready to risk our lives, defeat our'
                           ' foes, and maybe knock over some cups?',
                        2: 'Tell me the game plan again. Wait. Fish! '
                           'Someone has fish! Where is it?',
                        3: 'Cats make great companions! Just ask '
                           'my master... who disappeared under mys'
                           'terious circumstances.',
                        'after_food_msg':
                            f'nom..nom..nom. We reaaaaly need'
                            f' to get chicken on our menu too!',
                        'after_fav_food_msg':
                            'Yum.. My master knows me the best!',
                        'after_game_msg':
                            'Woohoo! Yuumi not bored anymore!',
                        'after_medicine_msg':
                            'Thank you master, next time I\'ll heal you!'}
