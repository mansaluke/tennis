import string
import random


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


class Side:
    """
    Side class used to track the details of each side (player or double)
    """
    def __init__(self, name: str=None):
        self.points: int = 0
        self.games_won: int = 0
        self.sets_won: int = 0
        self.matches_won: int = 0
        self.name = NameGenerator().check_unique_name(name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
