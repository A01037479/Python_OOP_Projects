from pet import Pet


class Teemo(Pet):
    """
    Teemo is a child class of Pet class.
    It is one of the pet species.
    """
    def __init__(self):
        """
        Instantiate a Teemo object, giving it specific properties and inherent from Pet
        """
        super().__init__()
        self.name = 'Teemo'
        self.health_decline_rate = 2
        self.hunger_increase_rate = 1
        self.happiness_decline_rate = 0.5
        self.health_standard = 70
        self.happiness_gain_rate = 5
        self.favorite_food = 'Mushroom'
        self.message = {1: 'Hump, two, three, four!', 2: 'Captain Teemo on duty!',
                        3: 'Never underestimate the power of the Scout\'s code.',
                        'after_food_msg': f'Not bad! Can I have some mushrooms too please?',
                        'after_fav_food_msg': 'Yummy master! Best food ever!',
                        'after_game_msg': 'Fun game! Play more!',
                        'after_medicine_msg': 'Thank you master, I feel a lot better now!'}
