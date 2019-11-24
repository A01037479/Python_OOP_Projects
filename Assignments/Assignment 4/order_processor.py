import enum
from cmath import nan

import pandas as pd
from factory import LuluLimeFactory, PineappleRepublicFactory, NikaFactory


class OrderProcessor:
    def __init__(self):
        self.orders_dict = None
        self.brand_factory_mapper = {'Lululime': LuluLimeFactory,
                                     'PineappleRepublic': PineappleRepublicFactory,
                                     'Nika': NikaFactory}

    def open_order_sheet(self, file_name):
        excel_data = pd.read_excel(file_name)
        self.orders_dict = excel_data.to_dict(orient='records')

    def process_next_order(self):
        for order_detail in self.orders_dict:
            formatted_order_detail = self.reformat(order_detail)
            factory = self.get_factory(formatted_order_detail['brand'])
            order = Order(formatted_order_detail, factory)
            yield order

    def get_factory(self, garment_type):
        factory = self.brand_factory_mapper[garment_type]
        return factory()

    def reformat(self, order_detail):
        formatted_order_detail = {}
        for key in order_detail.keys():
            # print(type(order_detail[key]), order_detail[key])
            new_key = key.lower().replace(' ', '_').replace('/', '_')
            formatted_order_detail[new_key] = order_detail[key]
            # if order_detail[key] == float(nan):
            #     formatted_order_detail[new_key] = 'N/A'
        return formatted_order_detail


class Order:
    def __init__(self, order_detail, factory):
        self.order_detail = order_detail
        self.factory = factory
