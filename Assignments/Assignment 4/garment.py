import enum
import datetime
from order_processor import OrderProcessor


# class GarmentType(enum.Enum):
#     ShirtMen = 'ShirtMen',
#     ShirtWomen = 'ShirtWomen',
#     SockPairUnisex = 'SockPairUnisex'


class GarmentMaker:
    def __init__(self):
        self.shirts_men = {}
        self.shirts_women = {}
        self.socks_unisex = {}
        self.order_processor = OrderProcessor()
        self.maker_mapper = {'ShirtMen': self.shirt_men_maker,
                             'ShirtWomen': self.shirt_women_maker,
                             'SockPairUnisex': self.socks_unisex_maker}



    def shirt_men_maker(self, shirt_men_order):
        order_detail = shirt_men_order.order_detail
        factory = shirt_men_order.factory
        count = shirt_men_order.order_detail['count']
        shirt = factory.create_shirt_men(**order_detail)
        self.shirts_men[shirt] = count

    def shirt_women_maker(self, shirt_women_order):
        order_detail = shirt_women_order.order_detail
        factory = shirt_women_order.factory
        count = shirt_women_order.order_detail['count']
        shirt = factory.create_shirt_women(**order_detail)
        self.shirts_women[shirt] = count

    def socks_unisex_maker(self, socks_unisex_order):
        order_detail = socks_unisex_order.order_detail
        factory = socks_unisex_order.factory
        count = socks_unisex_order.order_detail['count']
        shirt = factory.create_socks_unisex(**order_detail)
        self.socks_unisex[shirt] = count

    def print_daily_report(self):
        print(f'OOP Designs Inc. Factory Report '
              f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
        for shirt, count in self.shirts_men.items():
            print(f'\nOrder: {shirt.__class__.__name__}')
            for i in range(count):
                print(shirt)
        for shirt, count in self.shirts_women.items():
            print(f'\nOrder: {shirt.__class__.__name__}')
            for i in range(count):
                print(shirt)
        for socks, count in self.socks_unisex.items():
            print(f'\nOrder: {socks.__class__.__name__}')
            for i in range(count):
                print(socks)

def main():
    garment_maker = GarmentMaker()
    garment_maker.order_processor.open_order_sheet('COMP_3522_A4_orders.xlsx')

    for order in garment_maker.order_processor.process_next_order():
        # print(order.order_detail)
        garment_type = order.order_detail['garment']
        garment_maker.maker_mapper[garment_type](order)

    garment_maker.print_daily_report()


if __name__ == '__main__':
    main()
