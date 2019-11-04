import abc


class Pizza(abc.ABC):
    @abc.abstractmethod
    def add_ingredient(self):
        pass

    def check_out(self):
        pass


class BasePizza(Pizza):
    def __init__(self):
        self.crust = 'Signature Crust'
        self.cheese = None
        self.toppings = None
        self.price = 4.99

    def add_ingredient(self):
        pass

    def check_out(self):
        print(f'Total price: {self.price}')


class BasePizzaDecorator(Pizza):
    def __init__(self, base_pizza):
        self.base_pizza = base_pizza

    def add_ingredient(self):
        self.base_pizza.add_ingredient()

    def check_out(self):
        self.base_pizza.check_out()


class MozzarellaCheeseDecorator(BasePizzaDecorator):
    def add_ingredient(self):
        self.base_pizza.cheese.append = 'Mozzarella'
        self.base_pizza += 3.99

    def check_out(self):
        print(f'Added Mozzarella cheese for 3.99')
        super().check_out()


class MushroomsDecorator(BasePizzaDecorator):
    def add_ingredient(self):
        self.base_pizza.toppings.append = 'Mushrooms'
        self.base_pizza.price += 1.5

    def check_out(self):
        print(f'Added Mushrooms topping for 3.99')
        super().check_out()