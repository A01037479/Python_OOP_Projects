from card import Card
from expirable import Expirable


class StudentCard(Card, Expirable):
    def __init__(self):
        super().__init__()
        self.student_number = None
