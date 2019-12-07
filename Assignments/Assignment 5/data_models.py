"""
This module contains data models of pokemon, ability, move and stats.
"""
from abc import ABC


class DataModel(ABC):
    """
    Abstract class that represents a base data model that contains a name and id.
    """
    def __init__(self, name=None, id=None, **kwargs):
        self.name = name
        self.id = id

    def __str__(self):
        return f'--------{self.__class__.__name__}--------\nname: {self.name}' \
               f'\nid: {self.id}'


class Pokemon(DataModel):
    """
    Pokemon is a type of DataModel.
    """
    def __init__(self, height=None, weight=None, stats=None, types=None,
                 abilities=None, moves=None, **kwargs):
        super().__init__(**kwargs)
        self.height = height
        self.weight = weight
        self.stats = stats
        self.types = types
        self.abilities = abilities
        self.moves = moves

    def __str__(self):
        str_repr = f"{super().__str__()}" \
                   f"\nheight: {self.height}" \
                   f"\nweight: {self.weight}\n"
        str_repr += 'type: '
        for type in self.types:
            str_repr += '\n   ' + str(type)
        str_repr += '\nMoves:\n'
        for move in self.moves:
            str_repr += '   ' + str(move) + '\n'
        str_repr += 'Stats:\n'
        for stat in self.stats:
            str_repr += '   ' + str(stat) + '\n'
        str_repr += 'Abilities:\n'
        for ability in self.abilities:
            str_repr += '   ' + str(ability) + '\n'
        return str_repr


class Ability(DataModel):
    """
    Ability if a type of DataModel.
    """
    def __init__(self, generation=None, effect=None, short_effect=None,
                 pokemon=None, **kwargs):
        super().__init__(**kwargs)
        self.generation = generation
        self.effect = effect
        self.short_effect = short_effect
        self.pokemon = pokemon

    def __str__(self):
        return f"{super().__str__()}\ngeneration: {self.generation}" \
               f"\neffect: {self.effect}" \
               f"\neffect(short): {self.short_effect}" \
               f"\npokemon: {self.pokemon}\n"


class Move(DataModel):
    """
    Move if a type of DataModel.
    """
    def __init__(self, generation=None, accuracy=None, pp=None, power=None,
                 type=None, damage_class=None, short_effect=None,
                 level_learned_at=None, **kwargs):
        super().__init__(**kwargs)
        self.generation = generation
        self.accuracy = accuracy
        self.pp = pp
        self.power = power
        self.type = type
        self.damage_class = damage_class
        self.short_effect = short_effect
        self.level_learned_at = level_learned_at

    def __str__(self):
        return f'{super().__str__()}\ngeneration: {self.generation}' \
               f'\naccuracy: {self.accuracy}' \
               f'\npp: {self.pp}' \
               f'\npower: {self.power}\ntype: {self.type}' \
               f'\ndamage class: {self.damage_class}' \
               f'\neffect(short): {self.short_effect}' \
               f'\nlevel learned at: {self.level_learned_at}\n'


class Stat(DataModel):
    """
    Stat if a type of DataModel.
    """
    def __init__(self, is_battle_only=None, base_stat=None, **kwargs):
        super().__init__(**kwargs)
        self.is_battle_only = is_battle_only
        self.base_stat = base_stat

    def __str__(self):
        return f'{super().__str__()}\nis battle only: {self.is_battle_only}' \
               f'\nbase value: {self.base_stat}'
