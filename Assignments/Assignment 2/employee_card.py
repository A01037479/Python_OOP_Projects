from card import Card
from expirable import Expirable


class EmployeeCard(Card, Expirable):
    def __init__(self):
        super().__init__()
        self.job_title = None