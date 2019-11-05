from pizza import BasePizza, MozzarellaCheeseDecorator, \
    ParmigianoReggianoCheeseDecorator, VeganCheeseDecorator, \
    MushroomsDecorator, PineappleDecorator


class PizzaCompany:
    def __init__(self):
        self.pizza_order = None

    def take_pizza_order(self):
        print('Welcome to Python Pizza Company. All pizza starts '
              'at $4.99. Make your own pizza!')
        self.pizza_order = BasePizza()
        ordering = True
        while ordering:
            user_input = input(' 1.Add Cheese\n '
                               '2.Add Topping\n 3.Checkout\n')
            if user_input == '1':
                cheese_choice = input('Select cheese:')
                if cheese_choice == '1':
                    self.pizza_order = MozzarellaCheeseDecorator(
                        self.pizza_order)
                elif cheese_choice == '2':
                    self.pizza_order = ParmigianoReggianoCheeseDecorator(
                        self.pizza_order)
                elif cheese_choice == '3':
                    self.pizza_order = VeganCheeseDecorator(self.pizza_order)
                self.pizza_order.add_ingredient()
            elif user_input == '2':
                topping_choice = input('Select topping:')
                if topping_choice == '1':
                    self.pizza_order = MushroomsDecorator(self.pizza_order)
                elif topping_choice == '2':
                    self.pizza_order = PineappleDecorator(self.pizza_order)
                self.pizza_order.add_ingredient()
            elif user_input == '3':
                self.check_out_order()
            elif user_input == '4':
                ordering = False

    def check_out_order(self):
        if len(self.pizza_order.cheese) < 1:
            print('You need to add at least one cheese')
        elif len(self.pizza_order.toppings) < 1:
            print('You need to add at least one topping')
        else:
            self.pizza_order.print_receipt()


def main():
    pizza_company = PizzaCompany()
    pizza_company.take_pizza_order()


if __name__ == '__main__':
    main()
