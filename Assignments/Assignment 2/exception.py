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
