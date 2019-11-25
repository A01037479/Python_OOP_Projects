"""
This module contains the Abstract Factory Pattern for a garment factory.
"""
from abc import ABC


class BrandFactory(ABC):
    """
    BrandFactory defines the interface for three types of the garment that
    abstract factory pattern is responsible to create.
    """

    def create_shirt_men(self, **kwargs):
        pass

    def create_shirt_women(self, **kwargs):
        pass

    def create_socks_unisex(self, **kwargs):
        pass


class LuluLimeFactory(BrandFactory):
    """
    LuluLimeFactory is a type of BrandFactory that creates garment.
    """

    def create_shirt_men(self, **kwargs):
        return ShirtMenLuluLime(**kwargs)

    def create_shirt_women(self, **kwargs):
        return ShirtWomenLuluLime(**kwargs)

    def create_socks_unisex(self, **kwargs):
        return SockPairUnisexLuluLime(**kwargs)


class PineappleRepublicFactory(BrandFactory):
    """
    PineappleRepublicFactory is a type of BrandFactory that creates garment.
    """

    def create_shirt_men(self, **kwargs):
        return ShirtMenPineappleRepublic(**kwargs)

    def create_shirt_women(self, **kwargs):
        return ShirtWomenPineappleRepublic(**kwargs)

    def create_socks_unisex(self, **kwargs):
        return SockPairUnisexPineappleRepublic(**kwargs)


class NikaFactory(BrandFactory):
    """
    NikaFactory is a type of BrandFactory that creates garment.
    """

    def create_shirt_men(self, **kwargs):
        return ShirtMenNika(**kwargs)

    def create_shirt_women(self, **kwargs):
        return ShirtWomenNika(**kwargs)

    def create_socks_unisex(self, **kwargs):
        return SockPairUnisexNika(**kwargs)


class ShirtMen(ABC):
    """
    ShirtMen defines the interface for one kind of garment
    """

    def __init__(self, style_name=None, size=None, colour=None, textile=None,
                 **kwargs):
        self.style_name = style_name
        self.size = size
        self.colour = colour
        self.textile = textile
        if self.size.upper() not in ('S', 'M', 'L', 'XL', 'XXL'):
            raise ValueError('Invalid man shirt size, only S, M, L, XL, XXL.')

    def __str__(self):
        return f'Style name: {self.style_name}, Size {self.size},' \
               f' Colour: {self.colour}, Textile: {self.textile}'


class ShirtWomen(ABC):
    """
    ShirtWomen defines the interface for one kind of garment
    """

    def __init__(self, style_name=None, size=None, colour=None, textile=None,
                 **kwargs):
        self.style_name = style_name
        self.size = size
        self.colour = colour
        self.textile = textile
        if self.size.upper() not in ('XS', 'S', 'M', 'L', 'XL', 'XXL'):
            raise ValueError('Invalid woman shirt size, only XS, S, M, L, XL,'
                             ' XXL.')

    def __str__(self):
        return f'Style name: {self.style_name}, Size {self.size},' \
               f' Colour: {self.colour}, Textile: {self.textile}'


class SockPairUnisex(ABC):
    """
    SockPairUnisex defines the interface for one kind of garment
    """

    def __init__(self, style_name=None, size=None, colour=None, textile=None,
                 **kwargs):
        self.style_name = style_name
        self.size = size
        self.colour = colour
        self.textile = textile
        if self.size.upper() not in ('S', 'M', 'L'):
            raise ValueError('Invalid socks size, only S, M or L.')

    def __str__(self):
        return f'Style name: {self.style_name}, Size {self.size},' \
               f' Colour: {self.colour}, Textile: {self.textile}'


class ShirtMenLuluLime(ShirtMen):
    """
    ShirtMenLuluLime defines a type of ShirtMen garment
    """

    def __init__(self, sport=None, hidden_zipper_pockets=None, **kwargs):
        super().__init__(**kwargs)
        self.sport = sport
        self.hidden_zipper_pockets = hidden_zipper_pockets
        if not isinstance(self.hidden_zipper_pockets, float):
            raise ValueError('Number of pockets should be a number.')

    def __str__(self):
        return f'{super().__str__()}, Sport: {self.sport}' \
               f', Hidden Zipper pockets: {self.hidden_zipper_pockets}'


class ShirtMenPineappleRepublic(ShirtMen):
    """
    ShirtMenPineappleRepublic defines a type of ShirtMen garment
    """

    def __init__(self, buttons=None, requires_ironing=None, **kwargs):
        super().__init__(**kwargs)
        self.buttons = buttons
        self.requires_ironing = requires_ironing
        if not isinstance(self.buttons, float):
            raise ValueError('Number of buttons should be a number.')
        if self.requires_ironing.upper() not in ('Y', 'N'):
            raise ValueError('Requires ironing should be "Y" or "N".')

    def __str__(self):
        return f'{super().__str__()}, Buttons: {self.buttons},' \
               f' Requires Ironing {self.requires_ironing}'


class ShirtMenNika(ShirtMen):
    """
    ShirtMenNika defines a type of ShirtMen garment
    """

    def __init__(self, indoor_outdoor=None, **kwargs):
        super().__init__(**kwargs)
        self.indoor_outdoor = indoor_outdoor
        if self.indoor_outdoor.lower() not in ('indoor', 'outdoor'):
            raise ValueError('Indoor/Outdoor should be "indoor" or "outdoor".')

    def __str__(self):
        return f'{super().__str__()}, Indoor/Outdoor: {self.indoor_outdoor}'


class ShirtWomenLuluLime(ShirtWomen):
    """
    ShirtWomenLuluLime defines a type of ShirtWomen garment
    """

    def __init__(self, sport=None, hidden_zipper_pockets=None, **kwargs):
        super().__init__(**kwargs)
        self.sport = sport
        self.hidden_zipper_pockets = hidden_zipper_pockets
        if not isinstance(self.hidden_zipper_pockets, float):
            raise ValueError('Number of pockets should be a number.')

    def __str__(self):
        return f'{super().__str__()}, Sport: {self.sport},' \
               f' Hidden Zipper Pockets: {self.hidden_zipper_pockets}'


class ShirtWomenPineappleRepublic(ShirtWomen):
    """
    ShirtWomenPineappleRepublic defines a type of ShirtWomen garment
    """

    def __init__(self, buttons=None, requires_ironing=None, **kwargs):
        super().__init__(**kwargs)
        self.buttons = buttons
        self.requires_ironing = requires_ironing
        if not isinstance(self.buttons, float):
            raise ValueError('Number of buttons should be a number.')
        if self.requires_ironing.upper() not in ('Y', 'N'):
            raise ValueError('Requires ironing should be "Y" or "N".')

    def __str__(self):
        return f'{super().__str__()}, Buttons: {self.buttons},' \
               f' Requires Ironing: {self.requires_ironing}'


class ShirtWomenNika(ShirtWomen):
    """
    ShirtWomenNika defines a type of ShirtWomen garment
    """

    def __init__(self, indoor_outdoor=None, **kwargs):
        super().__init__(**kwargs)
        self.indoor_outdoor = indoor_outdoor
        if self.indoor_outdoor.lower() not in ('indoor', 'outdoor'):
            raise ValueError('Indoor/Outdoor should be "indoor" or "outdoor".')

    def __str__(self):
        return f'{super().__str__()}, Indoor/Outdoor: {self.indoor_outdoor}'


class SockPairUnisexLuluLime(SockPairUnisex):
    """
    SockPairUnisexLuluLime defines a type of SockPairUnisex garment
    """

    def __init__(self, silver=None, stripe=None, **kwargs):
        super().__init__(**kwargs)
        self.silver = silver
        self.stripe = stripe
        if self.silver.upper() not in ('Y', 'N'):
            raise ValueError('Silver be "Y" or "N".')

    def __str__(self):
        return f'{super().__str__()}, Silver: {self.silver},' \
               f' Stripe: {self.stripe}'


class SockPairUnisexPineappleRepublic(SockPairUnisex):
    """
    SockPairUnisexPineappleRepublic defines a type of SockPairUnisex garment
    """

    def __init__(self, dry_cleaning=None, **kwargs):
        super().__init__(**kwargs)
        self.dry_cleaning = dry_cleaning
        if self.dry_cleaning.upper() not in ('Y', 'N'):
            raise ValueError('Dry cleaning should be "Y" or "N".')

    def __str__(self):
        return f'{super().__str__()}, Dry Cleaning: {self.dry_cleaning}'


class SockPairUnisexNika(SockPairUnisex):
    """
    SockPairUnisexNika defines a type of SockPairUnisex garment
    """

    def __init__(self, articulated=None, length=None, **kwargs):
        super().__init__(**kwargs)
        self.articulated = articulated
        self.length = length
        if self.articulated.upper() not in ('Y', 'N'):
            raise ValueError('Articulated be "Y" or "N".')

    def __str__(self):
        return f'{super().__str__()}, Articulated: {self.articulated}, ' \
               f'Length: {self.length}'
