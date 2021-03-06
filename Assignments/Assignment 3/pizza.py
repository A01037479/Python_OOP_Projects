"""
The module contains pizza interface, base pizza class, base decorator and
decorator classes for cheese and toppings
"""
import abc
from ingredient import Cheese, Topping


class Pizza(abc.ABC):
    """
    Pizza interface. it describes basic behaviours and attributes of a pizza.
    """
    @abc.abstractmethod
    def __init__(self):
        self.crust = None
        self.cheese = {}
        self.toppings = {}
        self.total_price = None

    @abc.abstractmethod
    def add_ingredient(self):
        pass

    @abc.abstractmethod
    def print_receipt(self):
        pass

    @abc.abstractmethod
    def add_price(self, price):
        pass


class BasePizza(Pizza):
    """
    Base pizza class. It inherits from pizza interface.
    """
    def __init__(self):
        """
        Instantiates a base pizza with signature crust and starting price 4.99
        """
        super().__init__()
        self.crust = 'Signature Crust'
        self.total_price = 4.99

    def add_ingredient(self):
        pass

    def print_receipt(self):
        pass

    def add_price(self, price):
        pass


class BasePizzaDecorator(Pizza):
    """
    Base decorator class. It inherits from pizza interface. Decorates a
    pizza with an ingredient.
    """
    def __init__(self, base_pizza):
        """
        Instantiates a decorator that contains a pizza object.
        """
        super().__init__()
        self.ingredient = None
        self.ingredient_price = None
        self.crust = base_pizza.crust
        self.cheese = base_pizza.cheese
        self.toppings = base_pizza.toppings
        self.total_price = base_pizza.total_price

    def add_ingredient(self):
        """
        Adds the ingredient to the cheese or toppings list of pizza
        to decorate the pizza object.
        """
        if isinstance(self.ingredient, Cheese):
            if self.ingredient.name not in self.cheese.keys():
                self.cheese[self.ingredient.name] = 1
            else:
                self.cheese[self.ingredient.name] += 1
        elif isinstance(self.ingredient, Topping):
            if self.ingredient.name not in self.toppings.keys():
                self.toppings[self.ingredient.name] = 1
            else:
                self.toppings[self.ingredient.name] += 1
        self.add_price(self.ingredient_price)
        print('---------------------------------')
        print(f'Added one order of {self.ingredient.name} '
              f'{type(self.ingredient).__name__} for '
              f'${self.ingredient_price}!\n')
        print('You now have cheese:')
        if len(self.cheese) == 0:
            print(' None')
        else:
            for cheese, amount in self.cheese.items():
                print(f' {amount} x {cheese}')
        print('And toppings:')
        if len(self.toppings) == 0:
            print(' None')
        else:
            for topping, amount in self.toppings.items():
                print(f' {amount} x {topping}')
        print('---------------------------------')

    def add_price(self, price):
        """
        Adds the price to the total price of pizza object.
        :param price: int
        """
        self.total_price += price

    def print_receipt(self):
        """
        Prints out all the ingredients added and corresponding price.
        :return:
        """
        print('Added Signature crust for $4.99')
        for cheese, amount in self.cheese.items():
            print(f'Added {amount} x {cheese} cheese for '
                  f'${Cheese[cheese].value} each')
        for topping, amount in self.toppings.items():
            print(f'Added {amount} x {topping} topping for '
                  f'${Topping[topping].value} each')
        print(f'Total comes to ${self.total_price}')


class MozzarellaCheeseDecorator(BasePizzaDecorator):
    """
    Mozzarella cheese concrete decorator class. It inherits from base decorator.
    """
    def __init__(self, base_pizza):
        super().__init__(base_pizza)
        self.ingredient = Cheese.mozzarella
        self.ingredient_price = Cheese.mozzarella.value


class ParmigianoReggianoCheeseDecorator(BasePizzaDecorator):
    """
    ParmigianoReggiano cheese concrete decorator class.
    It inherits from base decorator.
    """
    def __init__(self, base_pizza):
        super().__init__(base_pizza)
        self.ingredient = Cheese.parmigianoreggiano
        self.ingredient_price = Cheese.parmigianoreggiano.value


class VeganCheeseDecorator(BasePizzaDecorator):
    """
    Vegan cheese concrete decorator class.
    It inherits from base decorator.
    """
    def __init__(self, base_pizza):
        super().__init__(base_pizza)
        self.ingredient = Cheese.vegan
        self.ingredient_price = Cheese.vegan.value


class MushroomsDecorator(BasePizzaDecorator):
    """
    Mushroom topping concrete decorator class.
    It inherits from base decorator.
    """
    def __init__(self, base_pizza):
        super().__init__(base_pizza)
        self.ingredient = Topping.mushrooms
        self.ingredient_price = Topping.mushrooms.value


class PeppersDecorator(BasePizzaDecorator):
    """
    Pepper topping concrete decorator class.
    It inherits from base decorator.
    """
    def __init__(self, base_pizza):
        super().__init__(base_pizza)
        self.ingredient = Topping.pepper
        self.ingredient_price = Topping.pepper.value


class PineappleDecorator(BasePizzaDecorator):
    """
    Pineapple topping concrete decorator class.
    It inherits from base decorator.
    """
    def __init__(self, base_pizza):
        super().__init__(base_pizza)
        self.ingredient = Topping.pineapple
        self.ingredient_price = Topping.pineapple.value


class FreshBasilDecorator(BasePizzaDecorator):
    """
    Fresh basil topping concrete decorator class.
    It inherits from base decorator.
    """
    def __init__(self, base_pizza):
        super().__init__(base_pizza)
        self.ingredient = Topping.freshBasil
        self.ingredient_price = Topping.freshBasil.value


class SpinachDecorator(BasePizzaDecorator):
    """
    spinach topping concrete decorator class.
    It inherits from base decorator.
    """
    def __init__(self, base_pizza):
        super().__init__(base_pizza)
        self.ingredient = Topping.spinach
        self.ingredient_price = Topping.spinach.value


class PepperoniDecorator(BasePizzaDecorator):
    """
    Pepperoni topping concrete decorator class.
    It inherits from base decorator.
    """
    def __init__(self, base_pizza):
        super().__init__(base_pizza)
        self.ingredient = Topping.pepperoni
        self.ingredient_price = Topping.pepperoni.value


class BeyondMeatDecorator(BasePizzaDecorator):
    """
    Beyond Meat topping concrete decorator class.
    It inherits from base decorator.
    """
    def __init__(self, base_pizza):
        super().__init__(base_pizza)
        self.ingredient = Topping.beyondMeat
        self.ingredient_price = Topping.beyondMeat.value
