from card import Card
from credit_card import CreditCard
from debit_card import DebitCard
from gift_card import GiftCard
from loyalty_card import LoyaltyCard
from membership_card import MembershipCard
from student_card import StudentCard
from employee_card import EmployeeCard


class CardGenerator:
    @staticmethod
    def create_debit_card(card_name, card_holder, issued_by):
        return DebitCard(card_name, card_holder, issued_by)

    @staticmethod
    def create_credit_card(card_name, card_holder, issued_by, issue_date,
                           expiry_date):
        return CreditCard(card_name, card_holder, issued_by, issue_date,
                          expiry_date)
