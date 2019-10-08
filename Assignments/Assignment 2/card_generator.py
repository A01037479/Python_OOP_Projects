from credit_card import CreditCard
from debit_card import DebitCard
from gift_card import GiftCard
from loyalty_card import LoyaltyCard
from membership_card import MembershipCard
from student_card import StudentCard
from employee_card import EmployeeCard
from expirable import Expirable


class CardGenerator:
    card_types = {'1': CreditCard, '2': DebitCard, '3': GiftCard,
                  '4': LoyaltyCard, '5': MembershipCard, '6': StudentCard,
                  '7': EmployeeCard}

    expirable_card_types = [card_type for card_type in card_types.values() if
                            issubclass(card_type, Expirable)]

    @staticmethod
    def create_debit_card(card_name, card_holder, issued_by):
        return DebitCard(card_name, card_holder, issued_by)

    @staticmethod
    def create_credit_card(card_name, card_holder, issued_by, issue_date,
                           expiry_date):
        return CreditCard(card_name, card_holder, issued_by, issue_date,
                          expiry_date)
