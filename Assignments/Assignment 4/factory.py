from abc import ABC


class BrandFactory(ABC):
    def create_shirt_men(self, **kwargs):
        pass

    def create_shirt_women(self, **kwargs):
        pass

    def create_socks_unisex(self, **kwargs):
        pass


class LuluLimeFactory(BrandFactory):
    def create_shirt_men(self, **kwargs):
        return ShirtMenLuluLime(**kwargs)

    def create_shirt_women(self, **kwargs):
        return ShirtWomenLuluLime(**kwargs)

    def create_socks_unisex(self, **kwargs):
        return SockPairUnisexLuluLime(**kwargs)


class PineappleRepublicFactory(BrandFactory):
    def create_shirt_men(self, **kwargs):
        return ShirtMenPineappleRepublic(**kwargs)

    def create_shirt_women(self, **kwargs):
        return ShirtWomenPineappleRepublic(**kwargs)

    def create_socks_unisex(self, **kwargs):
        return SockPairUnisexPineappleRepublic(**kwargs)


class NikaFactory(BrandFactory):
    def create_shirt_men(self, **kwargs):
        return ShirtMenNika(**kwargs)

    def create_shirt_women(self, **kwargs):
        return ShirtWomenNika(**kwargs)

    def create_socks_unisex(self, **kwargs):
        return SockPairUnisexNika(**kwargs)


class ShirtMen(ABC):
    def __init__(self, style_name=None, size=None, colour=None, textile=None,
                 **kwargs):
        self.style_name = style_name
        self.size = size
        self.colour = colour
        self.textile = textile

    def __str__(self):
        return f'{self.style_name}, {self.size}, {self.colour}, {self.textile}'


class ShirtWomen(ABC):
    def __init__(self, style_name=None, size=None, colour=None, textile=None,
                 **kwargs):
        self.style_name = style_name
        self.size = size
        self.colour = colour
        self.textile = textile

    def __str__(self):
        return f'{self.style_name}, {self.size}, {self.colour}, {self.textile}'


class SockPairUnisex(ABC):
    def __init__(self, style_name=None, size=None, colour=None, textile=None,
                 **kwargs):
        self.style_name = style_name
        self.size = size
        self.colour = colour
        self.textile = textile

    def __str__(self):
        return f'{self.style_name}, {self.size}, {self.colour}, {self.textile}'


class ShirtMenLuluLime(ShirtMen):
    def __init__(self, sport=None, hidden_zipper_pockets=None, **kwargs):
        super().__init__(**kwargs)
        self.sport = sport
        self.hidden_zipper_pockets = hidden_zipper_pockets

    def __str__(self):
        return f'{super().__str__()}, {self.sport}, {self.hidden_zipper_pockets}'


class ShirtMenPineappleRepublic(ShirtMen):
    def __init__(self, buttons=None, requires_ironing=None, **kwargs):
        super().__init__(**kwargs)
        self.buttons = buttons
        self.requires_ironing = requires_ironing

    def __str__(self):
        return f'{super().__str__()}, {self.buttons}, {self.requires_ironing}'


class ShirtMenNika(ShirtMen):
    def __init__(self, indoor_outdoor=None, **kwargs):
        super().__init__(**kwargs)
        self.indoor_outdoor = indoor_outdoor

    def __str__(self):
        return f'{super().__str__()}, {self.indoor_outdoor}'


class ShirtWomenLuluLime(ShirtWomen):
    def __init__(self, sport=None, hidden_zipper_pockets=None, **kwargs):
        super().__init__(**kwargs)
        self.sport = sport
        self.hidden_zipper_pockets = hidden_zipper_pockets

    def __str__(self):
        return f'{super().__str__()}, {self.sport}, {self.hidden_zipper_pockets}'


class ShirtWomenPineappleRepublic(ShirtWomen):
    def __init__(self, buttons=None, requires_ironing=None, **kwargs):
        super().__init__(**kwargs)
        self.buttons = buttons
        self.requires_ironing = requires_ironing

    def __str__(self):
        return f'{super().__str__()}, {self.buttons}, {self.requires_ironing}'


class ShirtWomenNika(ShirtWomen):
    def __init__(self, indoor_outdoor=None, **kwargs):
        super().__init__(**kwargs)
        self.indoor_outdoor = indoor_outdoor

    def __str__(self):
        return f'{super().__str__()}, {self.indoor_outdoor}'


class SockPairUnisexLuluLime(SockPairUnisex):
    def __init__(self, silver=None, stripe=None, **kwargs):
        super().__init__(**kwargs)
        self.silver = silver
        self.stripe = stripe

    def __str__(self):
        return f'{super().__str__()}, {self.silver}, {self.stripe}'


class SockPairUnisexPineappleRepublic(SockPairUnisex):
    def __init__(self, dry_cleaning=None, **kwargs):
        super().__init__(**kwargs)
        self.dry_cleaning = dry_cleaning

    def __str__(self):
        return f'{super().__str__()}, {self.dry_cleaning}'


class SockPairUnisexNika(SockPairUnisex):
    def __init__(self, articulated=None, length=None, **kwargs):
        super().__init__(**kwargs)
        self.articulated = articulated
        self.length = length

    def __str__(self):
        return f'{super().__str__()}, {self.articulated}, {self.length}'
