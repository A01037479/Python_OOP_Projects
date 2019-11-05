import abc
from ingredient import Cheese, Topping


class Pizza(abc.ABC):
    @abc.abstractmethod
    def add_ingredient(self):
        pass

    @abc.abstractmethod
    def print_receipt(self):
        pass


class BasePizza(Pizza):
    def __init__(self):
        self.crust = 'Signature Crust'
        self.cheese = {}
        self.toppings = {}
        self.total_price = 4.99

    def add_ingredient(self):
        pass

    def print_receipt(self):
        pass


class BasePizzaDecorator(Pizza):

    def __init__(self, base_pizza):
        self.ingredient = None
        self.ingredient_price = None
        self.base_pizza = base_pizza
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
        print(f'Your pizza now has cheese: {self.cheese}, toppings: '
              f'{self.toppings}')

    def add_price(self, price):
        self.total_price += price

    def print_receipt(self):
        print('Added Signature crust for $4.99')
        for cheese, price in self.cheese.items():
            print(f'Added {cheese} for ${price}')
        for topping, price in self.toppings.items():
            print(f'Added {topping} for ${price}')
        print(f'Total comes to ${self.total_price}')


class MozzarellaCheeseDecorator(BasePizzaDecorator):
    def __init__(self, base_pizza):
        super().__init__(base_pizza)
        self.ingredient = Cheese.mozzarella
        self.ingredient_price = Cheese.mozzarella.value


class ParmigianoReggianoCheeseDecorator(BasePizzaDecorator):
    def __init__(self, base_pizza):
        super().__init__(base_pizza)
        self.ingredient = Cheese.parmigiano_reggiano
        self.ingredient_price = 4.99


class VeganCheeseDecorator(BasePizzaDecorator):
    def __init__(self, base_pizza):
        super().__init__(base_pizza)
        self.ingredient = Cheese.mozzarella
        self.ingredient_price = 5.99


class MushroomsDecorator(BasePizzaDecorator):
    def add_ingredient(self):
        self.toppings.append('Mushrooms')
        self.total_price += 1.5
        super().add_ingredient()


class PeppersDecorator(BasePizzaDecorator):
    def add_ingredient(self):
        self.toppings.append('Peppers')
        self.total_price += 1.5
        super().add_ingredient()


class PineappleDecorator(BasePizzaDecorator):
    def add_ingredient(self):
        self.toppings.append('Pineapple')
        self.total_price += 2.0
        super().add_ingredient()


class PepperoniDecorator(BasePizzaDecorator):
    def add_ingredient(self):
        self.toppings.append('Ppperoni')
        self.total_price += 3.0
        super().add_ingredient()
