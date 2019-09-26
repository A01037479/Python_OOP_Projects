from pet import Pet


class Fizz(Pet):
    """
    Fizz class is a sub class of Pet. A Fizz is one species of pets.
    It inherits all the properties and methods from parent class.
    """
    def __init__(self):
        super().__init__()
        self.name = 'Fizz'
        self.health_decline_rate = 0.5
        self.hunger_increase_rate = 0.6
        self.happiness_decline_rate = 0.5
        self.health_standard = 60
        self.happiness_gain_rate = 8
        self.favorite_food = 'Crab meat'
        self.message = {1: 'To the briny deep!',
                        2: 'The mighty shark stalks his prey!',
                        3: 'I\'ll show them a watery grave!',
                        'after_food_msg':
                            f'nom..nom..I don\'t make request '
                            f'but can I have crab meat next time please?',
                        'after_fav_food_msg':
                            'I can really eat these '
                            'fresh crab meat for days!',
                        'after_game_msg':
                            'These games are fun, we should play everyday!',
                        'after_medicine_msg':
                            'Feeling stronger than ever!'}
