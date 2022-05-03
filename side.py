import string
import random
from dataclasses import dataclass
from typing import Optional
from enum import Enum, auto


class Points(Enum):
    POINT: int = auto()
    GAME: int = auto()
    SET: int = auto()
    MATCH: int = auto()


class Singleton(type):
    """
    Singleton metaclass
    """
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class NameGenerator(metaclass=Singleton):
    """
    lets give each side a name and ensure unique
    Using singleton metaclass we ensure no repeated names
    """
    names = []

    def __init__(self, name_length=3):
        self.name_length = name_length

    def check_unique_name(self, name) -> str:
        """
        returns name if unique. If not creates new one.
        """
        if name:
            if name in NameGenerator.names:
                print("Name taken. Assigning new one")
                name = self.create_new_name()
        else:
            name = self.create_new_name()
        return name

    def create_new_name(self) -> str:
        _new_name = ''.join(
            random.choice(string.ascii_letters) for x in range(self.name_length)
        )
        return self.check_unique_name(_new_name)


@dataclass
class Side:
    """
    Side class represents each side (single player or double)
    """
    name: Optional[str] = None
    points: Points.POINT = 0
    games_won: Points.GAME = 0
    sets_won: Points.SET = 0
    matches_won: Points.MATCH = 0

    def __post_init__(self):
        self.name: str = NameGenerator().check_unique_name(self.name)
