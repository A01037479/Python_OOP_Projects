from card import Card
from expirable import Expirable


class EmployeeCard(Card, Expirable):
    def __init__(self, card_name, card_holder, issued_by, issue_date,
                 expiry_date, job_title):
        super().__init__(card_name, card_holder, issued_by, issue_date,
                         expiry_date)
        self.job_title = job_title
