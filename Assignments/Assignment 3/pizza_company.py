from pizza import BasePizza, MozzarellaCheeseDecorator, \
    ParmigianoReggianoCheeseDecorator, VeganCheeseDecorator, \
    MushroomsDecorator, PeppersDecorator, PineappleDecorator, \
    FreshBasilDecorator, SpinachDecorator, PepperoniDecorator, \
    BeyondMeatDecorator

from ingredient import Cheese, Topping


class PizzaCompany:
    def __init__(self):
        self.pizza_order = None
        self.cheese_menu = {1: ParmigianoReggianoCheeseDecorator,
                            2: MozzarellaCheeseDecorator,
                            3: VeganCheeseDecorator}
        self.topping_menu = {1: MushroomsDecorator,
                             2: PeppersDecorator,
                             3: PineappleDecorator,
                             4: FreshBasilDecorator,
                             5: SpinachDecorator,
                             6: PepperoniDecorator,
                             7: BeyondMeatDecorator}

    def take_pizza_order(self):
        print('Welcome to Python Pizza Company. All pizza starts '
              'at $4.99. Make your own pizza!')
        self.pizza_order = BasePizza()
        ordering = True
        while ordering:
            user_input = input('\n 1.Add Cheese\n 2.Add Topping\n 3.Checkout\n'
                               ' 4.Exit store\n Your choice: ')
            if user_input == '1':
                print('\n Select cheese:')
                i = 1
                for cheese in Cheese:
                    print(f' {i}. {cheese.name}')
                    i += 1
                try:
                    cheese_choice = int(input(' Your Choice: '))
                    self.pizza_order = \
                        self.cheese_menu[cheese_choice](self.pizza_order)
                except KeyError:
                    print('\nPlease enter valid choice!')
                except ValueError:
                    print('\nPlease enter valid choice!')
                else:
                    self.pizza_order.add_ingredient()
            elif user_input == '2':
                print('\n Select toppings:')
                i = 1
                for topping in Topping:
                    print(f' {i}. {topping.name}')
                    i += 1
                try:
                    topping_choice = input(' Your Choice: ')
                    self.pizza_order = \
                        self.topping_menu[int(topping_choice)](
                            self.pizza_order)
                except KeyError:
                    print('\nPlease enter valid choice!')
                except ValueError:
                    print('\nPlease enter valid choice!')
                else:
                    self.pizza_order.add_ingredient()
            elif user_input == '3':
                ordering = not self.check_out_order()
            elif user_input == '4':
                ordering = False
            else:
                print('\nPlease enter valid choice!')

    def check_out_order(self):
        if len(self.pizza_order.cheese) < 1:
            print('\nYou need to add at least one cheese to check out!')
            return False
        elif len(self.pizza_order.toppings) < 1:
            print('\nYou need to add at least one topping to check out!')
            return False
        else:
            print('---------------------------------\nYour receipt: ')
            self.pizza_order.print_receipt()
            print('---------------------------------')
            return True


def main():
    pizza_company = PizzaCompany()
    pizza_company.take_pizza_order()


if __name__ == '__main__':
    main()
