import os
from unittest import TestCase
from unittest import mock
from controller import Controller
from card_manager import CardManager
from exception import InvalidCardTypeError, InvalidCardBalanceError, \
    InvalidDateFormatError, DuplicatedNameError, NameNotFoundError, \
    EmptyCardManagerError, InvalidSexError, InvalidHeightError, InvalidAgeError


class TestController(TestCase):
    """
    The class contains all test methods for add/remove/search/backup.
    """
    @mock.patch('controller.input', create=True)
    def test_user_add_card_invalid_card_type_integer(self, mocked_input):
        """
        Tests user_add_card when invalid card type(Integer) given.
        """
        mocked_input.side_effect = ['-1', 'done']
        Controller.card_manager = CardManager()
        self.assertRaises(InvalidCardTypeError, Controller.user_add_card)

    @mock.patch('controller.input', create=True)
    def test_user_add_card_invalid_card_type_string(self, mocked_input):
        """
        Tests user_add_card when invalid card type(String) given.
        """
        mocked_input.side_effect = ['my choice', 'done']
        Controller.card_manager = CardManager()
        self.assertRaises(InvalidCardTypeError, Controller.user_add_card)

    @mock.patch('controller.input', create=True)
    def test_user_add_card_invalid_balance_input(self, mocked_input):
        """
        Tests user_add_card when invalid card balance given.
        """
        mocked_input.side_effect = ['2', 'card a', 'eric', 'somewhere',
                                    '-100' 'done']
        Controller.card_manager = CardManager()
        self.assertRaises(InvalidCardBalanceError, Controller.user_add_card)

    @mock.patch('controller.input', create=True)
    def test_user_add_card_invalid_date_input(self, mocked_input):
        """
        Tests user_add_card when invalid date format given.
        """
        mocked_input.side_effect = ['4', 'card a', 'eric', 'somewhere',
                                    'Oct.6th.1919' 'done']
        Controller.card_manager = CardManager()
        self.assertRaises(InvalidDateFormatError, Controller.user_add_card)

    @mock.patch('controller.input', create=True)
    def test_user_add_card_invalid_age_input(self, mocked_input):
        """
        Tests user_add_card when invalid age given.
        """
        mocked_input.side_effect = ['6', 'Driver licence', 'eric',
                                    'government of Canada', '2000-12-12',
                                    '2020-12-12', 'A010xxx', '-10', 'done']
        Controller.card_manager = CardManager()
        self.assertRaises(InvalidAgeError, Controller.user_add_card)

    @mock.patch('controller.input', create=True)
    def test_user_add_card_invalid_sex_input(self, mocked_input):
        """
        Tests user_add_card when invalid sex given.
        """
        mocked_input.side_effect = ['6', 'Driver licence', 'eric',
                                    'government of Canada', '2000-12-12',
                                    '2020-12-12', 'A010xxx', '26', '179',
                                    'Boy', 'done']
        Controller.card_manager = CardManager()
        self.assertRaises(InvalidSexError, Controller.user_add_card)

    @mock.patch('controller.input', create=True)
    def test_user_add_card_invalid_height_input(self, mocked_input):
        """
        Tests user_add_card when invalid height input given.
        """
        mocked_input.side_effect = ['6', 'Driver licence', 'eric',
                                    'government of Canada', '2000-12-12',
                                    '2020-12-12', 'A010xxx', '26',
                                    'very tall', 'done']
        Controller.card_manager = CardManager()
        self.assertRaises(InvalidHeightError, Controller.user_add_card)

    @mock.patch('controller.input', create=True)
    def test_user_add_card_reward_card(self, mocked_input):
        """
        Tests user_add_card when a reward card is successfully added.
        """
        mocked_input.side_effect = ['1', 'Starbucks reward card', 'eric',
                                    'Starbucks', 'points', 'done']
        Controller.card_manager = CardManager()
        self.assertTrue(Controller.user_add_card)

    @mock.patch('controller.input', create=True)
    def test_user_add_card_balance_card(self, mocked_input):
        """
        Tests user_add_card when a balance card is successfully added.
        """
        mocked_input.side_effect = ['2', 'Compass Card', 'eric',
                                    'TransLink', '150', 'done']
        Controller.card_manager = CardManager()
        self.assertTrue(Controller.user_add_card)

    @mock.patch('controller.input', create=True)
    def test_user_add_card_Membership_card(self, mocked_input):
        """
        Tests user_add_card when a membership card is successfully added.
        """
        mocked_input.side_effect = ['3', 'YMCA card', 'eric', 'YMCA',
                                    '2012-12-12', '2013-12-12', 'regular',
                                    'done']
        Controller.card_manager = CardManager()
        self.assertTrue(Controller.user_add_card)

    @mock.patch('controller.input', create=True)
    def test_user_add_card_bank_card(self, mocked_input):
        """
        Tests user_add_card when a bank card is successfully added.
        """
        mocked_input.side_effect = ['4', 'BMO credit card', 'eric', 'BMO',
                                    '2012-12-12', '2013-12-12',
                                    'downtown branch', 'done']
        Controller.card_manager = CardManager()
        self.assertTrue(Controller.user_add_card)

    @mock.patch('controller.input', create=True)
    def test_user_add_card_id_card(self, mocked_input):
        """
        Tests user_add_card when a id card is successfully added.
        """
        mocked_input.side_effect = ['5', 'BCIT student card', 'eric', 'BCIT',
                                    '2012-12-12', '2013-12-12',
                                    'A01037479', 'done']
        Controller.card_manager = CardManager()
        self.assertTrue(Controller.user_add_card)

    @mock.patch('controller.input', create=True)
    def test_user_add_card_govID_card(self, mocked_input):
        """
        Tests user_add_card when a government id card is successfully added.
        """
        mocked_input.side_effect = ['6', 'Drivers licence', 'eric', 'ICBC',
                                    '2012-12-12', '2013-12-12', '123123123',
                                    '26', '179', 'Male', 'done']
        Controller.card_manager = CardManager()
        self.assertTrue(Controller.user_add_card)

    @mock.patch('controller.input', create=True)
    def test_user_add_card_other_card(self, mocked_input):
        """
        Tests user_add_card when an other type card is successfully added.
        """
        mocked_input.side_effect = ['7', 'Moive ticket', 'eric',
                                    'Scotia Bank theatre', 'Redeems one movie',
                                    'done']
        Controller.card_manager = CardManager()
        self.assertTrue(Controller.user_add_card)

    @mock.patch('controller.input', create=True)
    def test_user_remove_card_no_found(self, mocked_input):
        """
        Tests user_remove_card when no card result matches.
        """
        mocked_input.side_effect = ['BCIT student card', 'done']
        Controller.card_manager = CardManager()
        self.assertRaises(NameNotFoundError, Controller.user_remove_card)

    @mock.patch('controller.input', create=True)
    def test_user_remove_card_found(self, mocked_input):
        """
        Tests user_remove_card when a card is successfully removed.
        """
        mocked_input.side_effect = ['1', 'Starbucks reward card', 'eric',
                                    'Starbucks', 'points',
                                    'Starbucks reward card', 'done']
        Controller.card_manager = CardManager()
        Controller.user_add_card()
        self.assertTrue(Controller.user_remove_card)

    @mock.patch('controller.input', create=True)
    def test_user_search_card_no_found(self, mocked_input):
        """
        Tests user_search_card when no card result matches.
        """
        mocked_input.side_effect = ['BCIT student card', 'done']
        Controller.card_manager = CardManager()
        self.assertRaises(NameNotFoundError, Controller.user_search_card)

    @mock.patch('controller.input', create=True)
    def test_user_search_card_found(self, mocked_input):
        """
        Tests user_search_card when a card is successfully searched.
        """
        mocked_input.side_effect = ['1', 'Starbucks reward card', 'eric',
                                    'Starbucks', 'points',
                                    'Starbucks reward card', 'done']
        Controller.card_manager = CardManager()
        Controller.user_add_card()
        self.assertTrue(Controller.user_search_card)

    def test_user_back_up_data(self):
        """
        Tests user_back_up_card when card manager is empty.
        """
        Controller.card_manager = CardManager()
        self.assertRaises(EmptyCardManagerError, Controller.user_backup_data)

    @mock.patch('controller.input', create=True)
    def test_user_back_up_data_success(self, mocked_input):
        """
        Tests user_back_up_card when successfully backed up.
        """
        mocked_input.side_effect = ['1', 'Starbucks reward card', 'eric',
                                    'Starbucks', 'points', 'done']
        Controller.card_manager = CardManager()
        Controller.user_add_card()
        file_path = Controller.user_backup_data()
        self.assertTrue(os.path.exists(file_path))