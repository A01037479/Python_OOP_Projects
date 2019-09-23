class Food:
    recover_amount = 20

    @classmethod
    def feed(cls, pet):
        if pet.favorite_food == cls:
            pet.lower_hunger(cls.recover_amount * 1.1)
        else:
            pet.lower_hunger(cls.recover_amount)
