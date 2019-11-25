"""
This module contains OrderProcessor that deals with Order objects.
"""
import pandas as pd
from garment_abstract_factory import LuluLimeFactory, PineappleRepublicFactory, NikaFactory


class OrderProcessor:
    """
    OrderProcessor reads from a excel sheet of order details and creates orders.
    It contains a orders dictionary and a mapper to the BrandFactory classes.
    """
    def __init__(self):
        self.orders_data_frame = None
        self.brand_factory_mapper = {'Lululime': LuluLimeFactory,
                                     'PineappleRepublic': PineappleRepublicFactory,
                                     'Nika': NikaFactory}

    def open_order_sheet(self, file_name):
        self.orders_data_frame = pd.read_excel(file_name)

    def process_next_order(self):
        """
        A generator that yields next Order object in the orders dictionary.
        :return: Order
        """
        for order_detail in self.orders_data_frame.to_dict(orient='records'):
            formatted_order_detail = self.reformat(order_detail)
            factory = self.get_factory(formatted_order_detail['brand'])
            order = Order(formatted_order_detail, factory)
            yield order

    def get_factory(self, brand_type):
        try:
            factory = self.brand_factory_mapper[brand_type]
        except KeyError:
            print('No factory found for invalid brand type')
        else:
            return factory()

    def reformat(self, order_detail):
        formatted_order_detail = {}
        for key in order_detail.keys():
            new_key = key.lower().replace(' ', '_').replace('/', '_')
            formatted_order_detail[new_key] = order_detail[key]
        return formatted_order_detail


class Order:
    """
    Order contains order details read from OrderProcessor and a factory
    reference to a factory class.
    """
    def __init__(self, order_detail, factory):
        self.order_detail = order_detail
        self.factory = factory
