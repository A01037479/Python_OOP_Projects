import enum


class Cheese(enum.Enum):
    parmigianoreggiano = 4.99
    mozzarella = 3.99
    vegan = 5.99


class Topping(enum.Enum):
    mushrooms = 1.6
    pepper = 1.5
    pineapple = 2.0
    freshBasil = 2.5
    spinach = 1.0
    pepperoni = 3.0
    beyondMeat = 4.0
