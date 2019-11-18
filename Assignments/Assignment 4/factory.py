from abc import ABC


class BrandFactory(ABC.abc):
    def create_shirt_men(self):
        pass

    def create_shirt_women(self):
        pass

    def create_socks_unisex(self):
        pass


class LuluLimeFactory(BrandFactory):
    def create_shirt_men(self):
        return ShirtMenLuluLime()

    def create_shirt_women(self):
        return ShirtWomenLuluLime()

    def create_socks_unisex(self):
        return SockPairUnisexLuluLime()


class PineappleRepublicFactory(BrandFactory):
    def create_shirt_men(self):
        return ShirtMenPineappleRepublic()

    def create_shirt_women(self):
        return ShirtWomenPineappleRepublic()

    def create_socks_unisex(self):
        return SockPairUnisexPineappleRepublic()


class NikaFacotory(BrandFactory):
    def create_shirt_men(self):
        return ShirtMenNika()

    def create_shirt_women(self):
        return ShirtWomenNika()

    def create_socks_unisex(self):
        return SockPairUnisexNika()


class ShirtMen(ABC.abc):
    def __init__(self):
        self.style = None
        self.size = None
        self.colour = None
        self.textile = None


class ShirtWomen(ABC.abc):
    def __init__(self):
        self.style = None
        self.size = None
        self.colour = None
        self.textile = None


class SockPairUnisex(ABC.abc):
    def __init__(self):
        self.style = None
        self.size = None
        self.colour = None
        self.textile = None


class ShirtMenLuluLime(ShirtMen):
    def __init__(self):
        super().__init__()
        self.yoga_or_running = None
        self.num_of_pockets = None


class ShirtMenPineappleRepublic(ShirtMen):
    def __init__(self):
        super().__init__()
        self.requires_ironing = None
        self.num_of_buttons = None


class ShirtMenNika(ShirtMen):
    def __init__(self):
        super().__init__()
        self.indoor_or_outdoor = None


class ShirtWomenLuluLime(ShirtWomen):
    def __init__(self):
        super().__init__()
        self.yoga_or_running = None
        self.num_of_pockets = None


class ShirtWomenPineappleRepublic(ShirtWomen):
    def __init__(self):
        super().__init__()
        self.requires_ironing = None
        self.num_of_buttons = None


class ShirtWomenNika(ShirtWomen):
    def __init__(self):
        super().__init__()
        self.indoor_or_outdoor = None


class SockPairUnisexLuluLime(SockPairUnisex):
    def __init__(self):
        super().__init__()
        self.contains_silver = None
        self.color_of_stripe = None


class SockPairUnisexPineappleRepublic(SockPairUnisex):
    def __init__(self):
        super().__init__()
        self.requires_dry_clean = None


class SockPairUnisexNika(SockPairUnisex):
    def __init__(self):
        super().__init__()
        self.is_articulated = None
        self.length = None
