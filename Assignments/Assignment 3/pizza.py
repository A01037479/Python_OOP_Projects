import abc
from ingredient import Cheese, Topping


class Pizza(abc.ABC):
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
    def __init__(self):
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

    def __init__(self, base_pizza):
        super().__init__()
        self.ingredient = None
        self.ingredient_price = None
        self.crust = base_pizza.crust
        self.cheese = base_pizza.cheese
        self.toppings = base_pizza.toppings
        self.total_price = base_pizza.total_price

    def add_ingredient(self):
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
        print(f'Added one {self.ingredient.name} for '
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
        self.total_price += price

    def print_receipt(self):
        print('Added Signature crust for $4.99')
        for cheese, amount in self.cheese.items():
            print(f'Added {amount} x {cheese}')
        for topping, amount in self.toppings.items():
            print(f'Added {amount} x {topping}')
        print(f'Total comes to ${self.total_price}')


class MozzarellaCheeseDecorator(BasePizzaDecorator):
    def __init__(self, base_pizza):
        super().__init__(base_pizza)
        self.ingredient = Cheese.mozzarella
        self.ingredient_price = Cheese.mozzarella.value


class ParmigianoReggianoCheeseDecorator(BasePizzaDecorator):
    def __init__(self, base_pizza):
        super().__init__(base_pizza)
        self.ingredient = Cheese.parmigianoreggiano
        self.ingredient_price = Cheese.parmigianoreggiano.value


class VeganCheeseDecorator(BasePizzaDecorator):
    def __init__(self, base_pizza):
        super().__init__(base_pizza)
        self.ingredient = Cheese.vegan
        self.ingredient_price = Cheese.vegan.value


class MushroomsDecorator(BasePizzaDecorator):
    def __init__(self, base_pizza):
        super().__init__(base_pizza)
        self.ingredient = Topping.mushrooms
        self.ingredient_price = Topping.mushrooms.value


class PeppersDecorator(BasePizzaDecorator):
    def __init__(self, base_pizza):
        super().__init__(base_pizza)
        self.ingredient = Topping.pepper
        self.ingredient_price = Topping.pepper.value


class PineappleDecorator(BasePizzaDecorator):
    def __init__(self, base_pizza):
        super().__init__(base_pizza)
        self.ingredient = Topping.pineapple
        self.ingredient_price = Topping.pineapple.value


class FreshBasilDecorator(BasePizzaDecorator):
    def __init__(self, base_pizza):
        super().__init__(base_pizza)
        self.ingredient = Topping.freshBasil
        self.ingredient_price = Topping.freshBasil.value


class SpinachDecorator(BasePizzaDecorator):
    def __init__(self, base_pizza):
        super().__init__(base_pizza)
        self.ingredient = Topping.spinach
        self.ingredient_price = Topping.spinach.value


class PepperoniDecorator(BasePizzaDecorator):
    def __init__(self, base_pizza):
        super().__init__(base_pizza)
        self.ingredient = Topping.pepperoni
        self.ingredient_price = Topping.pepperoni.value


class BeyondMeatDecorator(BasePizzaDecorator):
    def __init__(self, base_pizza):
        super().__init__(base_pizza)
        self.ingredient = Topping.beyondMeat
        self.ingredient_price = Topping.beyondMeat.value
