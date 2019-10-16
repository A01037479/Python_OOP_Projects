"""
The module contains all custom exceptions.
"""


class InvalidCardTypeError(Exception):
    def __init__(self):
        super().__init__('Invalid card type!')


class InvalidCardBalanceError(Exception):
    def __init__(self):
        super().__init__('Card balance should be non-negative numbers!')


class InvalidDateFormatError(Exception):
    def __init__(self):
        super().__init__('Please enter date in format YYYY-MM-DD!')


class DuplicatedNameError(Exception):
    def __init__(self):
        super().__init__('The card name already exists.')


class NameNotFoundError(Exception):
    def __init__(self):
        super().__init__('The card name can not be found.')


class EmptyCardManagerError(Exception):
    def __init__(self):
        super().__init__('Card Manager does not have any card stored.')


class InvalidAgeError(Exception):
    def __init__(self):
        super().__init__('Age should be 0 to 99.')


class InvalidHeightError(Exception):
    def __init__(self):
        super().__init__('Height must be positive number.')


class InvalidSexError(Exception):
    def __init__(self):
        super().__init__('Sex must be male or female.')
