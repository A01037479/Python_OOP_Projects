from abc import ABC


class DataModel(ABC):
    def __init__(self, name=None, id=None, generation=None, **kwargs):
        self.name = name
        self.id = id
        self.generation = generation

    def __str__(self):
        return f'{self.__class__.__name__}:\nname: {self.name}' \
               f'\nid: {self.id}\ngeneration: {self.generation}'


class Pokemon(DataModel):
    def __init__(self, height=None, weight=None, stats=None, types=None,
                 abilities=None, moves=None, **kwargs):
        super().__init__(**kwargs)
        self.height = height
        self.weight = weight
        self.stats = stats
        self.types = types
        self.abilities = abilities
        self.moves = moves


class Ability(DataModel):
    def __init__(self, effect=None, short_effect=None, pokemon=None, **kwargs):
        super().__init__(**kwargs)
        self.effect = effect
        self.short_effect = short_effect
        self.pokemon = pokemon

    def __str__(self):
        return f'{super().__str__()}\neffect: {self.effect}' \
               f'\neffect(short): {self.short_effect}' \
               f'\npokemon: {self.pokemon}\n'


class Move(DataModel):
    def __init__(self, accuracy=None, pp=None, power=None, type=None,
                 damage_class=None, short_effect=None, **kwargs):
        super().__init__(**kwargs)
        self.accuracy = accuracy
        self.pp = pp
        self.power = power
        self.type = type
        self.damage_class = damage_class
        self.short_effect = short_effect

    def __str__(self):
        return f'{super().__str__()}\naccuracy: {self.accuracy}' \
               f'\npp: {self.pp}' \
               f'\npower: {self.power}\ntype: {self.type}' \
               f'\ndamage class: {self.damage_class}' \
               f'\neffect(short): {self.short_effect}\n'


class Stats:
    def __init__(self, name, base_stat, url):
        self.name = name
        self.base_stat = base_stat
        self.url = url
