from card import Card
from expirable import Expirable


class CreditCard(Card, Expirable):
    def __init__(self, card_name, card_holder, issued_by, issue_date,
                 expiry_date):
        Card.__init__(self, card_name, card_holder, issued_by)
        Expirable.__init__(self, issue_date, expiry_date)
