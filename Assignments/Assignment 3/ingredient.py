import enum


class Cheese(enum.Enum):
    parmigiano_reggiano = 4.99
    mozzarella = 3.99
    vegan = 5.99


class Topping(enum.Enum):
    pepper = 1.5
    pineapple = 2.0
    mushrooms = 1.5
    freshBasil = 2.0
    spinach = 1.0
    pepperoni = 3.0
    beyondMeat = 4.0