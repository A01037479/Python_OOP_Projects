from unittest import TestCase
from unittest import mock
from controller import Controller
from card_manager import CardManager
from exception import InvalidCardTypeError, InvalidCardBalanceError, \
    InvalidDateFormatError, DuplicatedNameError, NameNotFoundError, \
    EmptyCardManagerError, InvalidSexError, InvalidHeightError, InvalidAgeError


class TestController(TestCase):
    @mock.patch('controller.input', create=True)
    def test_user_add_card_first_input_invalid_integer(self, mocked_input):
        mocked_input.side_effect = ['-1', 'done']
        Controller.card_manager = CardManager()
        self.assertRaises(InvalidCardTypeError, Controller.user_add_card)

    @mock.patch('controller.input', create=True)
    def test_user_add_card_first_input_string(self, mocked_input):
        mocked_input.side_effect = ['my choice', 'done']
        Controller.card_manager = CardManager()
        self.assertRaises(InvalidCardTypeError, Controller.user_add_card)
