from card import Card
from expirable import Expirable


class StudentCard(Card, Expirable):
    def __init__(self, student_number, card_name, card_holder, issued_by,
                 issue_date, expiry_date):
        super().__init__(card_name, card_holder, issued_by, issue_date,
                         expiry_date)
        self.student_number = student_number
