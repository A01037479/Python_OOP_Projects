from card import Card
from expirable import Expirable


class CreditCard(Card, Expirable):
    def __init__(self):
        super().__init__()