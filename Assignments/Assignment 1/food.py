class Food:
    recover_amount = 20
    favored_recover_amount = 22
    food_dct = {'1': 'Mushroom', '2': 'Crab meat', '3': 'Chicken'}

    @classmethod
    def feed(cls, pet, food_choice):
        if cls.food_dct[food_choice] == pet.favorite_food:
            pet.lower_hunger(cls.favored_recover_amount)
        else:
            pet.lower_hunger(cls.recover_amount)
