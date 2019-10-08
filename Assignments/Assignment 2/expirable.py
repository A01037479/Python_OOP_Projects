from abc import ABC


class Expirable(ABC):
    def __init__(self, issue_date, expiry_date):
        self.issue_date = issue_date
        self.expiry_date = expiry_date
