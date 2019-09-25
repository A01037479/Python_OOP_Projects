class Food:
    """
    Static class that represents food. It contains class variables:
     a dictionary of food types and amount of hunger recovery.
    """
    recover_amount = 20
    favored_recover_amount = 22
    food_dct = {'1': 'Mushroom', '2': 'Crab meat', '3': 'Chicken'}

    @classmethod
    def feed(cls, pet, food_choice):
        """
        Takes in food choice to search from food dictionary and lower
        pet's hunger level according to specific food choice
        :param pet: Pet (Fizz, Teemo, Yuumi)
        :param food_choice: String
        """
        if cls.food_dct[food_choice] == pet.favorite_food:
            pet.lower_hunger(cls.favored_recover_amount)
        else:
            pet.lower_hunger(cls.recover_amount)
