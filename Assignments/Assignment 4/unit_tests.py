from unittest import TestCase
from pandas import DataFrame
from order_processor import OrderProcessor, Order
from garment_abstract_factory import LuluLimeFactory, ShirtMen
from garment_maker import GarmentMaker


class TestOrderProcessor(TestCase):
    def test_open_order_sheet(self):
        """
        Tests if the method open_order_sheet reads an excel sheet and returns
        a DataFrame object.
        """
        order_processor = OrderProcessor()
        order_processor.open_order_sheet('COMP_3522_A4_orders.xlsx')
        self.assertTrue(self, isinstance(order_processor.orders_data_frame,
                                         DataFrame))

    def test_process_next_order(self):
        """
        Tests if the method process_next_order returns a Order object.
        """
        order_processor = OrderProcessor()
        order_processor.open_order_sheet('COMP_3522_A4_orders.xlsx')
        next_order = next(order_processor.process_next_order())
        self.assertTrue(self, isinstance(next_order, Order))

    def test_get_factory(self):
        """
        Tests get_factory method when valid brand option is provided.
        """
        order_processor = OrderProcessor()
        factory = order_processor.get_factory('Lululime')
        self.assertTrue(self, isinstance(factory, LuluLimeFactory))

    def test_get_factory_invalid(self):
        """
        Tests get_factory method when invalid brand type is given.
        """
        order_processor = OrderProcessor()
        self.assertRaises(KeyError,
                          order_processor.get_factory('AppleRepublic'))

    def test_shirt_men_maker(self):
        """
        Tests if shirt_men_maker method creates an ShirtMen object and stores
        it into garment maker.
        """
        garment_maker = GarmentMaker()
        garment_maker.order_processor = OrderProcessor()
        garment_maker.order_processor.open_order_sheet(
            'COMP_3522_A4_orders.xlsx')
        next_order = next(garment_maker.order_processor.process_next_order())
        garment_maker.shirt_men_maker(next_order)

        self.assertTrue(self, isinstance(next(iter(garment_maker.shirts_men)),
                                         ShirtMen))
